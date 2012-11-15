#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import pygame
from pygame.locals import *
from pygame import * # this is needed for init
init() # starts pygame - "initialise"?
#intialisation of variables and objects.
RIGHT = 1
STOP = 0
LEFT = -1
screen = pygame.display.set_mode((640, 480))
font = font.Font(None, 32) # Font object 'None' = system default, size 48
intransit=False

def winLoseCheck(farmerPosition,cabbagePosition,sheepPosition,wolfPosition): # checks to see if your a loser by looking at the locations of the different objects and seeing if unallowed combinations occur ie wolf+sheep with no farmer	
	lose = 0
	if cabbagePosition.left>=484 and sheepPosition.left>=484 and wolfPosition.left>=484 and farmerPosition.left>=484: #if all of the items are passed point 484 then you've won
		textToScreen("Well Done!",screen,435)
		pygame.mixer.Sound('win.wav').play()
		lose += 3
	
	if farmerPosition.left>=484 and sheepPosition.left<=95 and wolfPosition<=95 and cabbagePosition<=95:
		#textToScreen("fail, you moved out on your own",screen,400)
		lose += 1
	
	if cabbagePosition.left>=484 and sheepPosition.left>=484 and farmerPosition.left<=100:		#C and S on left
		textToScreen("Fail, cabbage and sheep on the right",screen,400)
		lose += 1
		
	
	if cabbagePosition.left<=100 and sheepPosition.left<=100 and farmerPosition.left>=484:	#C and S on right
		textToScreen("Fail, cabbage and sheep on the left",screen,400)
		lose += 1
	
	if wolfPosition.left>=484 and sheepPosition.left>=484 and farmerPosition.left<=100:		#W and S on left
		textToScreen("Fail, wolf and sheep on the right",screen,435)
		lose += 1
	
	if wolfPosition.left<=100 and sheepPosition.left<=100 and farmerPosition.left>=484:	#W and S on right
		textToScreen("Fail, wolf and sheep on the left",screen,435)
		lose += 1
		
	if lose == 1 or lose==2:
		pygame.mixer.Sound('lose.wav').play()
		textToScreen("You lost - Game restarting",screen,460)
		pygame.time.delay(3500)
		main() # restarts main game loop
	elif lose == 3:
		textToScreen("You won - game restarting",screen,460)
		pygame.time.delay(3500)
		main() # restarts main game loop
		

def main():
	#screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('River Crossing Game') # sets window title
	global intransit
	
	
	
	farmer = pygame.image.load('farmer.png').convert_alpha()
	background = pygame.image.load('background4.bmp').convert_alpha()
	screen.blit(background, (0, 0)) #draw the background screen
	farmerPosition = pygame.Rect(100,50,67,100)
	screen.blit(farmer, farmerPosition) #draw the farmer
	farmerMove= STOP


	
	#print farmerPosition
	wolf = pygame.image.load('wolf.png').convert_alpha()
	wolfPosition = pygame.Rect(100,150,100,62)
	screen.blit(wolf, wolfPosition) #draw the wolf
	wolfMove=STOP
	
	sheep = pygame.image.load('sheep.png').convert_alpha()
	sheepPosition = pygame.Rect(100,250,100,100)
	screen.blit(sheep, sheepPosition) #draw the goat
	sheepMove=STOP
	
	cabbage = pygame.image.load('cabbage.png').convert_alpha()
	cabbagePosition = pygame.Rect(100,350,80,82)
	screen.blit(cabbage, cabbagePosition) #draw the cabbage
	cabbageMove=STOP

	pygame.display.update() #display all 
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# Check for key press
				
				if event.key== pygame.K_q:#quits the game
						sys.exit()
						
							
#				if event.key== pygame.K_t: # Display some text
#					text()
				
#				if event.key== pygame.K_a:#does very little 
#						printText("hi",screen)
				if event.key == pygame.K_h:		#show help screen
					helpScreen()
					screen.blit(background, (0, 0))
					updateScreen(screen)
					
				if event.key == pygame.K_f:
				  # if key pressed is 'f' key, move farmer (check if moving from left to right or other way)
					if farmerMove == STOP and farmerPosition.left > 483 and intransit==False:
						farmerMove = LEFT
						pygame.mixer.Sound('farmer.wav').play()
					elif farmerMove == STOP and farmerPosition.left < 101 and intransit==False:
						farmerMove = RIGHT
						pygame.mixer.Sound('farmer.wav').play()
				if event.key == pygame.K_c:
				  # if key pressed is 'C' key, move CABBAGE (check if moving from left to right or other way)
					
					if cabbageMove == STOP and cabbagePosition.left > 483 and farmerPosition.left >101 and intransit==False:
						cabbageMove = LEFT
						farmerMove=LEFT
						pygame.mixer.Sound('Cabbage.wav').play()
					elif cabbageMove == STOP and cabbagePosition.left < 483 and farmerPosition.left <101 and intransit==False:					
						cabbageMove = RIGHT 
						farmerMove=RIGHT
						pygame.mixer.Sound('Cabbage.wav').play()		
						
				if event.key == pygame.K_w:
				  # if key pressed is 'W' key, move WOLF (check if moving from left to right or other way)
					if wolfMove == STOP and wolfPosition.left > 483 and farmerPosition.left >101 and intransit==False:
						wolfMove = LEFT
						farmerMove=LEFT
						pygame.mixer.Sound('Howl.wav').play()
					elif wolfMove == STOP and wolfPosition.left < 483 and farmerPosition.left <483 and intransit==False:
						wolfMove = RIGHT
						farmerMove=RIGHT
						pygame.mixer.Sound('Howl.wav').play()
						
				if event.key == pygame.K_s:
				  # if key pressed is 'S' key, move SHEEP (check if moving from left to right or other way)
					if sheepMove == STOP and sheepPosition.left > 101 and farmerPosition.left >483 and intransit==False:
						sheepMove = LEFT
						farmerMove=LEFT
						pygame.mixer.Sound('Baa.wav').play()
					elif sheepMove == STOP and sheepPosition.left < 483 and farmerPosition.left <483 and intransit==False:
						sheepMove = RIGHT
						farmerMove=RIGHT
						pygame.mixer.Sound('Baa.wav').play()
						
		#this section for animating the farmer
		if (farmerMove == RIGHT):
			if (farmerPosition.left <= (540 - 60)):
				farmerPosition = farmerPosition.move(5, 0) # move farmer
				intransit=True
			else:
				farmerMove = STOP
				intransit=False
		if (farmerMove == LEFT):
			if (farmerPosition.left >= (100)):
				farmerPosition = farmerPosition.move(-5, 0) # move farmer
				intransit=True
			else:
				farmerMove = STOP
				intransit=False
		moveMe(farmer,farmerPosition,screen)	
		
		#this section for animating the cabbage
		if (cabbageMove == RIGHT):
			if (cabbagePosition.left <= (540 - 60)):
				cabbagePosition = cabbagePosition.move(5, 0) # move farmer
				intransit=True
			else:
				cabbageMove = STOP
				intransit=False
		if (cabbageMove == LEFT):
			if (cabbagePosition.left >= (100)):
				cabbagePosition = cabbagePosition.move(-5, 0) # move farmer
				intransit=True
			else:
				cabbageMove = STOP
				intransit=False
		moveMe(cabbage,cabbagePosition,screen)		
		
		#this section for animating the sheep
		if (sheepMove == RIGHT):
			if (sheepPosition.left <= (540 - 60)):
				sheepPosition = sheepPosition.move(5, 0) # move farmer
				intransit=True
			else:
				sheepMove = STOP
				intransit=False
		if (sheepMove == LEFT):
			if (sheepPosition.left >= (100)):
				sheepPosition = sheepPosition.move(-5, 0) # move farmer
				intransit=True
			else:
				sheepMove = STOP
				intransit=False
				
		moveMe(sheep,sheepPosition,screen)
		
		#this section for animating the wolf		
		if (wolfMove == RIGHT):
			if (wolfPosition.left <= (540 - 60)):
				wolfPosition = wolfPosition.move(5, 0) # move farmer
				intransit=True
			else:
				wolfMove = STOP
				intransit=False
		if (wolfMove == LEFT):
			if (wolfPosition.left >= (100)):
				wolfPosition = wolfPosition.move(-5, 0) # move farmer
				intransit=True
				
			else:
				wolfMove = STOP
				intransit=False
		moveMe(wolf,wolfPosition,screen)
				
		updateScreen(screen)	#updates screen once for all items preventing eplilectic fits.
		
		screen.blit(background, cabbagePosition, cabbagePosition)# erase cabbage animation
		screen.blit(background, farmerPosition, farmerPosition) # erase farmer  animation
		screen.blit(background, wolfPosition, wolfPosition) # erase wolf  animation
		screen.blit(background, sheepPosition, sheepPosition) # erase sheep  animation
		
		#checks to make sure you haven't lost yet
		winLoseCheck(farmerPosition,cabbagePosition,sheepPosition,wolfPosition)
		
def updateScreen(screen):	#updates screen once instead of for every item
	pygame.display.update()  # and show it all
	pygame.time.delay(20)  # stop the program for 1/100 second

def moveMe(item,position,screen): #function to move the different items.
	screen.blit(item, position) # draw new item
	
def textToScreen(text,screen,y):	#function used to print text to the screen. text is text to display, screen is needed for bliting and y is the vertical co-ordinate.
	screen=screen
	text=text
	text1 = font.render(text, True, (50, 255, 50)) # RGB, true Anti-Alias
	screen.blit(text1, (10, y)) # plots the text (horiz, vert)
	display.update()

def titleScreen():	#displays the title screen
	title = pygame.image.load('Scan4.png').convert_alpha()
	screen.blit(title, (0, 0)) #draw the background screen
	pygame.display.update()
	pygame.time.delay(2000) 

def helpScreen():	#displays the help screen then waits for user to press h to continue
	title = pygame.image.load('help.bmp').convert_alpha()
	screen.blit(title, (0, 0)) #draw the background screen
	pygame.display.update()
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					return
					

titleScreen()		#displays title screen once at beginning.			
	
if __name__ == '__main__':
    main()
