#!/usr/bin/env python

# CM1101 Game Task - River Crossing Problem
# Group 11
# Code by Tom Ashworth & Ryan McIntyre

import sys, os, pygame, math, time, random, copy
from pygame.locals import *
pygame.init()

# Question storage & testing class
class Question:
	def __init__(self, text):
		self.text = text
		self.answers = []
	def add(self, answer):
		self.answers.append(answer)
	def out(self):
		print self.text
		for a in self.answers:
			print a
	def ask(self):
		print self.text
	def test(self, input):
		if str(input).lower().strip() in self.answers:
			return True
		return False

class Actor:
	# Constructor
	def __init__(self, name, image, positions, level, sf):
		self.name = name
		self.image = pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(),(int(125 * sf),int(125 * sf)))
		self.positions = positions # array of possible positions with funny ordering, see below
		self.state = -1
		self.level = level
		self.width = self.image.get_width()
		self.height = self.image.get_height()
	def draw(self, screen):
		if self.state != 0:
			screen.blit(self.image, self.positions[self.state])
	# Check to see if click was within image area
	def check_mouse(self, position):
		click = pygame.Rect(position,(2,2))
		img = self.image.get_rect()
		if pygame.Rect(self.positions[self.state],(img.width, img.height)).contains(click):
			return True
	def click(self):
		self.state *= -1

class Boat():
	def __init__(self, image, side, level, positions):
		self.image = pygame.image.load(image).convert_alpha()
		self.side = side
		self.level = level
		self.positions = positions # array of possible positions with funny ordering, see below
		self.location = self.positions[self.level][self.side]
		self.direction = -1
		self.moving = False
		self.steps = 0
		self.scalar = 1 # current scale factor
		self.speed = 20 # number of animation steps
		self.move_step = [0,0]
		self.scale_step = 0
		self.scales = [0.5,0.7,1] # scale factors for each level
		self.next_level = level
		self.next_side = side
		self.pickup = False
		self.dropoff = False
		self.pause = False
		self.actor = False
	def draw(self, screen):
		if self.side not in [0, self.direction]: # always face the center of the river
			self.image = pygame.transform.flip(self.image, True, False)
			self.direction *= -1
		width = int(self.image.get_width() * self.scalar)
		height = int(self.image.get_height() * self.scalar)
		loc = self.positions[self.level][self.side]
		if self.moving == False: # lock onto previously defined locations to prevent drift
			self.location = self.positions[self.level][self.side]
		else: 
			loc = self.location
		screen.blit(pygame.transform.smoothscale(self.image,(width, height)), loc)
	def check_mouse(self, position):
		# was that click on me?
		click = pygame.Rect(position,(2,2))
		img = self.image.get_rect()
		if pygame.Rect(self.location,(img.width, img.height)).contains(click):
			return True
	def move(self, point):
		self.moving = True
		
		# work out direction of travel
		movex = self.positions[point[0]][point[1]][0] - self.positions[self.level][self.side][0]
		movey = self.positions[point[0]][point[1]][1] - self.positions[self.level][self.side][1]

		# find magnitude of direction vector
		mag = math.sqrt(movex ** 2 + movey ** 2)
		
		# create a movement vector, and limit it to max speed if neccessary
		move = [movex, movey]
		if mag > self.speed:
			move = [(movex / mag) * (mag / self.speed), (movey / mag) * (mag / self.speed)]
		# store this movement vector
		self.move_step = move

		# create a small value for scaling the image
		self.scale_step = (self.scales[point[0]] - self.scales[self.level]) / self.speed

		# store where we should be next
		self.next_level = point[0]
		self.next_side = point[1]
		# print "target ", self.positions[self.next_level][self.next_side]
		# print "location ", self.location
		
		if mag < 5:
			self.steps = 21
	def update(self):
		if self.pause: # stop briefly during pickup
			self.actor.state = 0
			time.sleep(0.5)
			self.pause = False
		if self.steps > self.speed: # movement finished?
			self.steps = 0
			self.level = self.next_level
			self.side = self.next_side
			self.moving = False
			if self.dropoff:
				self.dropoff = False
				self.actor.state = self.next_side
			if self.pickup: # when it's a pickup, start a new movement immediately
				self.pickup = False
				self.dropoff = True
				self.move([self.level, self.side * -1])
				self.pause = True
		else:
			# this only runs if we are actively moving
			self.steps += 1
			self.scalar += self.scale_step
			# update location
			self.location = (self.location[0] + int(round(self.move_step[0])), self.location[1] + int(round(self.move_step[1])))
			print "location ", self.location
	def goto(self, actor):
		self.pickup = True
		self.actor = actor
		self.move([actor.level, actor.state])
		
def check(actors, boat, rules, moves):
	total = 0
	for a in actors: # cycle through actors simulating a cross-checking table
		total += a.state
		for b in actors:
			if a.name == b.name: # wolf can't eat itself
				continue
			if rules[a.name] == b.name and a.state == b.state and boat.side != a.state:
				return "Oh no! The " + a.name + " ate the " + b.name + "!"
	if total == 3: # win!
		return "Woo, everyone safely crossed. It took " + str(moves) + " moves!"
	return True
	
def question(questions, moves, questionbox, screen, font, static):
	boxoffset = (1024 - questionbox.get_width()) / 2
	
	index = random.randint(0,len(questions)-1)
	q = questions.pop(index)
	
	text = q.text
	textoffset = (1024 - font.size(text)[0]) / 2
	answer = ""
	
	ticks = 0
	tspeed = 20
	
	answered = False
	while not answered:
		ticks += 1
		for event in pygame.event.get():
			if event.type is KEYDOWN:
				if event.key is K_RETURN:
					answered = True
				elif event.key is K_BACKSPACE:
					answer = answer[:-1]
				elif event.key is K_ESCAPE:
					return False
				else:
					answer += event.unicode
			if event.type is QUIT:
				pygame.quit()
				return False
		buf = answer
		if ticks > tspeed:
			buf += "|"
		if ticks > tspeed * 2:
			ticks = 0
		screen.blit(static,(0,0))
		screen.blit(questionbox,(boxoffset,50))
		screen.blit(font.render(text,True,(80,80,80)), (textoffset,90))
		screen.blit(font.render(text,True,(255,255,255)), (textoffset,90))
		screen.blit(font.render(buf,True,(255,255,255)), (220,165))
		pygame.display.update()
	
	if q.test(answer):
		return True
	else:
		return False
		
	return False
		
def main():
	
	# Initialise pygame
	screen = pygame.display.set_mode((1024,768),pygame.NOFRAME)
	pygame.display.set_caption('Cross the River')
	
	# Create background and actor objects
	background = pygame.image.load('bg-noref.png').convert_alpha()
	
	# popup and question boxes
	signbox = pygame.image.load('sign.png').convert_alpha()
	questionbox = pygame.image.load('question.png').convert_alpha()
	
	# init fonts
	font = pygame.font.Font("Chalkduster.ttf",28)
	
	# init questions
	try:
		file = open('questions.txt')
	except:
		pygame.quit()
		print "File could not be opened."
	
	# set up question array with Question objects
	questions = []
	temp = False
	for line in file:
		if line[0] == 'Q':
			if temp != False:
				questions.append(temp)
			temp = Question(line[2:-1])
			q = True
		elif line[0] == 'A':
			ans = line[2:-1]
			temp.add(ans.lower().strip())
	questions.append(temp)
	
	# create a copy of the questions for if we run out
	original_questions = copy.deepcopy(questions)
	
	# associative dictionary for applying rules
	rules = {
		'wolf' : 'sheep',
		'sheep' : 'cabbage',
		'cabbage' : ''
	}	
	
	# set up the animals
	actors = [					#    0			1			-1
		Actor("wolf", "Wolf.png", [(-100,-100), (814,425), (58,425)], 2, 1),
		Actor("sheep", "Sheep.png", [(-100,-100), (736,363), (167,366)], 1, 0.7),
		Actor("cabbage", "Cabbage.png", [(-100,-100), (678,319), (250,319)], 0, 0.5)
	]
	
	boat_positions = [
		#    0			1			-1
		[(488, 470),(549, 364),(319, 364)], # 0
		[(481, 480),(584, 414),(254, 414)], # 1
		[(468, 541),(606, 522),(176, 522)]  # 2
	]
	
	# build a boat
	boat = Boat("Boat2.png", -1, 2, boat_positions)
	
	controls = {
		"120" : (2,-1),
		"99" : (2,0),
		"118" : (2,1),
		"100" : (1,-1),
		"102" : (1,0),
		"103" : (1,1),
		"101" : (0,-1),
		"114" : (0,0),
		"116" : (0,1)
	}
	
	moves = 0
	allow_controls = False
	static = False
		
	# Game loop. Booyah.
	end = False
	repeat = False
	while not end:
		result = check(actors,boat,rules,moves)
		if result != True:
			offset = (1024 - font.size(result)[0]) / 2
			screen.blit(font.render(result,True,(80,80,80)), (offset,222))
			screen.blit(font.render(result,True,(255,255,255)), (offset,220))
			pygame.display.update()
			break
		# Handle events
		for event in pygame.event.get():
			if event.type is MOUSEBUTTONDOWN and not boat.moving: # clicky click
				# print event.pos
				for a in actors:
					if a.check_mouse(event.pos): # allow clicks on animals if the boat isn't moving
						if len(questions) < 3:
							questions = copy.deepcopy(original_questions)
						if question(questions, moves, questionbox, screen, font, static): # ask a question
							moves += 1
							result = "Correct! +1 moves"
						else:
							moves += 2
							result = "Wrong! +2 moves"
						offset = (1024 - font.size(result)[0]) / 2
						screen.blit(font.render(result,True,(80,80,80)), (offset,302))
						screen.blit(font.render(result,True,(255,255,255)), (offset,300))
						pygame.display.update()
						time.sleep(1)
						boat.goto(a) # off we go to the animal
			if event.type is KEYDOWN and allow_controls:
				if not boat.moving:
					print controls[str(event.key)]
					boat.move(controls[str(event.key)])
			if event.type is QUIT: # leaving us so soon?
				end = True
		if boat.moving:
			boat.update()
		# Draw
		screen.blit(background, (0,0))
		offset = (1024 - font.size("Moves: " + str(moves))[0]) / 2
		screen.blit(font.render("Moves: " + str(moves),True,(80,80,80)), (offset,12))
		screen.blit(font.render("Moves: " + str(moves),True,(255,255,255)), (offset,10))
		for a in actors:
			a.draw(screen)
		boat.draw(screen)
		static = screen.copy()
		pygame.display.update()
	
	quit = False
	while not quit:
		for event in pygame.event.get():
			if event.type in [MOUSEBUTTONDOWN, KEYDOWN, QUIT]:
				quit = True
				pygame.quit()
				break

# Beam me up, Scottie...
main()