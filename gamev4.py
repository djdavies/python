#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import pygame
from pygame.locals import * # to get text working

RIGHT = 1 # moves 1 to the right
STOP = 0
LEFT = -1 # moves 1 to the left

# ----------------Drawing, plotting, screen, etc----------------------------
def main():
	pygame.display.set_caption('Jake\'s Game')
	screen = pygame.display.set_mode((640, 480))
	farmer = pygame.image.load('farmer.bmp').convert()
	background = pygame.image.load('Background.bmp').convert()
	screen.blit(background, (0, 0)) #draw the background screen
	farmerPosition = pygame.Rect(100,50,75,60)
	screen.blit(farmer, farmerPosition) #draw the farmer
	farmerMove= STOP
	
	print farmerPosition
	wolf = pygame.image.load('wolf.bmp').convert()
	wolfPosition = pygame.Rect(100,150,75,60)
	screen.blit(wolf, wolfPosition) #draw the wolf
	wolfMove=STOP
	
	sheep = pygame.image.load('goat.bmp').convert()
	sheepPosition = pygame.Rect(100,250,75,60)
	screen.blit(sheep, sheepPosition) #draw the goat
	sheepMove=STOP
	
	cabbage = pygame.image.load('cabbage.bmp').convert()
	cabbagePosition = pygame.Rect(100,350,75,60)
	screen.blit(cabbage, cabbagePosition) #draw the cabbage
	cabbageMove=STOP
	
	pygame.display.update() #display all elements

	move = STOP
# ----------------------------------------------------------------------------
# -----------MAIN GAME LOOP---------------------------------------------------
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit() # checks for quit
			elif event.type == pygame.KEYDOWN:
				# Check for key press
				
				if event.key== pygame.K_q:#quits the game
						sys.exit()
						
						
				if event.key== pygame.K_a: # text on screen test
						printText("hi",screen)
	
		
				if event.key == pygame.K_f:
				  # if key pressed is 'f' key, move farmer (check if moving from left to right or other way)
					if move == STOP and farmerPosition.left > 300:
						move = LEFT
					elif move == STOP and farmerPosition.left < 300:
						move = RIGHT
						
				if event.key == pygame.K_c:
				  # if key pressed is 'C' key, move CABBAGE (check if moving from left to right or other way)
					if cabbageMove == STOP and cabbagePosition.left > 300 and move == STOP and farmerPosition.left > 300:
						cabbageMove = LEFT
						move = LEFT # causes farmer to move as well
					elif cabbageMove == STOP and cabbagePosition.left < 300 and move == STOP and farmerPosition.left < 300:
						cabbageMove = RIGHT
						move = RIGHT # farmer move too
							
				if event.key == pygame.K_w:
				  # if key pressed is 'W' key, move WOLF (check if moving from left to right or other way)
					if wolfMove == STOP and wolfPosition.left > 300 and move == STOP and farmerPosition.left > 300:
						wolfMove = LEFT
						move = LEFT
					elif wolfMove == STOP and wolfPosition.left < 300 and move == STOP and farmerPosition.left < 300:
						wolfMove = RIGHT
						move = RIGHT
						
				if event.key == pygame.K_s:
				  # if key pressed is 'S' key, move SHEEP (check if moving from left to right or other way)
					if sheepMove == STOP and sheepPosition.left > 300 and move == STOP and farmerPosition.left > 300:
						sheepMove = LEFT
						move = LEFT
					elif sheepMove == STOP and sheepPosition.left < 300 and move == STOP and farmerPosition.left < 300:
						sheepMove = RIGHT
						move = RIGHT
						
		#this section for animating the farmer
		
		if (move == RIGHT):
			if (farmerPosition.left <= (540 - 60)):
				farmerPosition = farmerPosition.move(5, 0) # move farmer
			else:
				move = STOP
		if (move == LEFT):
			if (farmerPosition.left >= (100)):
				farmerPosition = farmerPosition.move(-5, 0) # move farmer
			else:
				move = STOP
		moveMe(farmer,farmerPosition,screen)	
		
		#this section for animating the cabbage
		
		if (cabbageMove == RIGHT):
			if (cabbagePosition.left <= (540 - 60)):
				cabbagePosition = cabbagePosition.move(5, 0) # move farmer
				
			else:
				cabbageMove = STOP
		if (cabbageMove == LEFT):
			if (cabbagePosition.left >= (100)):
				cabbagePosition = cabbagePosition.move(-5, 0) # move farmer
				
			else:
				cabbageMove = STOP					
		moveMe(cabbage,cabbagePosition,screen)		
		
		#this section for animating the sheep
		
		if (sheepMove == RIGHT):
			if (sheepPosition.left <= (540 - 60)):
				sheepPosition = sheepPosition.move(5, 0) # move farmer
				
			else:
				sheepMove = STOP
		if (sheepMove == LEFT):
			if (sheepPosition.left >= (100)):
				sheepPosition = sheepPosition.move(-5, 0) # move farmer
				
			else:
				sheepMove = STOP					
		moveMe(sheep,sheepPosition,screen)
		
		#this section for animating the wolf
		
		if (wolfMove == RIGHT):
			if (wolfPosition.left <= (540 - 60)):
				wolfPosition = wolfPosition.move(5, 0) # move farmer
				
			else:
				wolfMove = STOP
		if (wolfMove == LEFT):
			if (wolfPosition.left >= (100)):
				wolfPosition = wolfPosition.move(-5, 0) # move farmer
				
			else:
				wolfMove = STOP					
		moveMe(wolf,wolfPosition,screen)
		
		
		
		updateScreen(screen)	#updates screen once for all items preventing eplilectic fits.
		
		
		screen.blit(background, cabbagePosition, cabbagePosition)# erase
		screen.blit(background, farmerPosition, farmerPosition) # erase
		screen.blit(background, wolfPosition, wolfPosition) # erase
		screen.blit(background, sheepPosition, sheepPosition) # erase
		#screen.blit(farmer, farmerPosition) # draw new farmer
		#pygame.display.update()  # and show it all
		#pygame.time.delay(10)  # stop the program for 1/100 second

	
def updateScreen(screen):	#updates screen once instead of for every item
	pygame.display.update()  # and show it all
	pygame.time.delay(20)  # stop the program for 1/100 second

def moveMe(item,position,screen): #function to move the different items.
	screen.blit(item, position) # draw new item
	#pygame.display.update()  # and show it all
	#pygame.time.delay(20)  # stop the program for 1/100 second
	print position
	
	
def printText(text,screen): #print text to screen
	i=1
	# Fill background
	pygame.font.init()
	text=text #pass argument to text variable
	font = pygame.font.Font(None, 36)
	text = font.render(text, 1, (255,255,255))
	#textpos = text.get_rect()
	textpos=320
	
	screen.blit(text,100,10,10)
	
#def winLoseCheck(farmerPosition.left,cabbagePosition.left,sheepPosition.left,wolfPosition.left): # checks to see if you're a loser	
#	if cabbagePosition.left>=540 and sheepPosition.left>=540 and farmerPosition.left<=100:		
#		print "fail, cabbage and sheep on the right"

if __name__ == '__main__':
    main()
