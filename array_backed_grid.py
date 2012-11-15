# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

# This sets the width and height of each grid location
width=20
height=20

# This sets the margin between each cell
margin=5

# Create a 2 dimensional array. A two dimesional
# array is simply a list of lists.
grid=[]
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0) # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Initialize pygame
pygame.init()
 
# Set the height and width of the screen
size=[255,255]
screen=pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column=pos[0] // (width+margin)
            row=pos[1] // (height+margin)
            # Sete t hat location to zero
            grid[row][column]=1
            print("Click ",pos,"Grid coordinates: ",row,column)

    # Set the screen background
    screen.fill(black)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
    
    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

