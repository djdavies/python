#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import pygame

RIGHT = 1
STOP = 0
LEFT = -1

def main():
    screen = pygame.display.set_mode((640, 480))
    farmer = pygame.image.load('farmer.bmp').convert()
    background = pygame.image.load('background.png').convert()
    screen.blit(background, (0, 0)) #draw the background screen
    farmerPosition = pygame.Rect(100,50,75,60)
    screen.blit(farmer, farmerPosition) #draw the farmer

    wolf = pygame.image.load('wolf.bmp').convert()
    wolfPosition = pygame.Rect(100,150,75,60)
    screen.blit(wolf, wolfPosition) #draw the wolf

    goat = pygame.image.load('goat.bmp').convert()
    goatPosition = pygame.Rect(100,250,75,60)
    screen.blit(goat, goatPosition) #draw the goat

    cabbage = pygame.image.load('cabbage.bmp').convert()
    cabbagePosition = pygame.Rect(100,350,75,60)
    screen.blit(cabbage, cabbagePosition) #draw the cabbage


    pygame.display.update() #display all elements

    move = RIGHT
    while 1:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             sys.exit()
          elif event.type == pygame.KEYDOWN:
				# Check for key press
              if event.key == pygame.K_f:
				  # if key pressed is 'f' key, move farmer (check if moving from left to right or other way)
                  if move == STOP and farmerPosition.left > 300:
                      move = LEFT
                  elif move == STOP and farmerPosition.left < 300:
                      move = RIGHT

       screen.blit(background, farmerPosition, farmerPosition) # erase
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
       screen.blit(farmer, farmerPosition) # draw new farmer
       pygame.display.update()  # and show it all
       pygame.time.delay(10)  # stop the program for 1/100 second



if __name__ == '__main__':
    main()

