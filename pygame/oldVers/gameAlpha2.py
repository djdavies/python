#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import pygame
from pygame.locals import *
import time # trying to pause before restart/lose game

RIGHT = 1
STOP = 0
LEFT = -1

def text():
	# Initialise screen
	pygame.init()

	# Fill background
	background = pygame.Surface(screen.get_size())

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

if __name__ == '__text__': text()

def winLoseCheck(farmerPosition,cabbagePosition,sheepPosition,wolfPosition): # checks to see if your a loser by looking at the locations of the different objects and seeing if unallowed combinations occur ie wolf+sheep with no farmer	
	#print "CP:" +str(cabbagePosition)+"Sp:"+str(sheepPosition)
	lose = 0
	
	if cabbagePosition.left>=484 and sheepPosition.left>=484 and wolfPosition.left>=484 and farmerPosition.left>=484: #if all of the items are passed point 484 then you've won
		print "Well Done!"
		lose += 2
	
	if farmerPosition.left>=484 and sheepPosition.left<=95 and wolfPosition<=95 and cabbagePosition<=95:
		print "fail, you moved out on your own"
		lose += 1
	
	if cabbagePosition.left>=484 and sheepPosition.left>=484 and farmerPosition.left<=100:		#C and S on left
		print "fail, cabbage and sheep on the right"
		lose += 1
		
	
	if cabbagePosition.left<=100 and sheepPosition.left<=100 and farmerPosition.left>=484:	#C and S on right
		print "fail, cabbage and sheep on the left"
		lose += 1
		#print (lose)
	
	if wolfPosition.left>=484 and sheepPosition.left>=484 and farmerPosition.left<=100:		#W and S on left
		print "fail, wolf and sheep on the right"
		lose += 1
	
	if wolfPosition.left<=100 and sheepPosition.left<=100 and farmerPosition.left>=484:	#W and S on right
		print "fail, wolf and sheep on the left"
		lose += 1
		
	if lose == 1:
		print "you lost - Game restarting"
		pygame.time.delay(2500)
		main() # restarts main game loop
	elif lose == 2:
		print"You won - game restarting"
		pygame.time.delay(2500)
		main() # restarts main game loop
		

def main():
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('River Crossing Game') # sets window title
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
	
	farmerCarry="" #not used at the minute

	pygame.display.update() #display all elements

	farmerMove = STOP
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# Check for key press
				
				if event.key== pygame.K_q:#quits the game
						sys.exit()
				
				if event.key== pygame.K_a:#does very little 
						printText("hi",screen)
				
				if event.key == pygame.K_f:
				  # if key pressed is 'f' key, move farmer (check if moving from left to right or other way)
					if farmerMove == STOP and farmerPosition.left > 300:
						farmerMove = LEFT
					elif farmerMove == STOP and farmerPosition.left < 300:
						farmerMove = RIGHT
						
				if event.key == pygame.K_c:
				  # if key pressed is 'C' key, move CABBAGE (check if moving from left to right or other way)
					
					if cabbageMove == STOP and cabbagePosition.left > 300 and farmerPosition.left >300:
						cabbageMove = LEFT
						farmerMove=LEFT
					elif cabbageMove == STOP and cabbagePosition.left < 300 and farmerPosition.left <300:
						cabbageMove = RIGHT 
						farmerMove=RIGHT
							
				if event.key == pygame.K_w:
				  # if key pressed is 'W' key, move WOLF (check if moving from left to right or other way)
					if wolfMove == STOP and wolfPosition.left > 300 and farmerPosition.left >300:
						wolfMove = LEFT
						farmerMove=LEFT
					elif wolfMove == STOP and wolfPosition.left < 300 and farmerPosition.left <300:
						wolfMove = RIGHT
						farmerMove=RIGHT
						
				if event.key == pygame.K_s:
				  # if key pressed is 'S' key, move SHEEP (check if moving from left to right or other way)
					if sheepMove == STOP and sheepPosition.left > 300 and farmerPosition.left >300:
						sheepMove = LEFT
						farmerMove=LEFT
					elif sheepMove == STOP and sheepPosition.left < 300 and farmerPosition.left <300:
						sheepMove = RIGHT
						farmerMove=RIGHT
						
		#this section for animating the farmer
		
		if (farmerMove == RIGHT):
			if (farmerPosition.left <= (540 - 60)):
				farmerPosition = farmerPosition.move(5, 0) # move farmer
			else:
				farmerMove = STOP
		if (farmerMove == LEFT):
			if (farmerPosition.left >= (100)):
				farmerPosition = farmerPosition.move(-5, 0) # move farmer
			else:
				farmerMove = STOP
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
		
		
		screen.blit(background, cabbagePosition, cabbagePosition)# erase cabbage animation
		screen.blit(background, farmerPosition, farmerPosition) # erase farmer  animation
		screen.blit(background, wolfPosition, wolfPosition) # erase wolf  animation
		screen.blit(background, sheepPosition, sheepPosition) # erase sheep  animation
		#screen.blit(farmer, farmerPosition) # draw new farmer
		#pygame.display.update()  # and show it all
		#pygame.time.delay(10)  # stop the program for 1/100 second
		
		#checks to make sure you haven't lost yet

		winLoseCheck(farmerPosition,cabbagePosition,sheepPosition,wolfPosition)
		#winLoseCheck()
		
def updateScreen(screen):	#updates screen once instead of for every item
	pygame.display.update()  # and show it all
	pygame.time.delay(20)  # stop the program for 1/100 second


def moveMe(item,position,screen): #function to move the different items.
	screen.blit(item, position) # draw new item
	#pygame.display.update()  # and show it all
	#pygame.time.delay(20)  # stop the program for 1/100 second
	
	
	
def printText(text,screen): #print text to screen NOT USED AT THE MINUTE
	i=1
	# Fill background
	pygame.font.init()
	text=text #pass argument to text variable
	font = pygame.font.Font(None, 36)
	text = font.render(text, 1, (255,255,255))
	#textpos = text.get_rect()
	textpos=320
	
	screen.blit(text,100,10,10)
	


if __name__ == '__main__':
    main()
