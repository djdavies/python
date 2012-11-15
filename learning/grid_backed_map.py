# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

width=20
height=20
margin=5

# --- Create grid of numbers
# Create an empty list
grid = []
# Loop for each row
for row in range(10):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(10):
        # Add a number to the current row
        grid[row].append(0)

# Set row 1, column 5 to zero
grid[1][5] = 1
    
pygame.init()
 
screen_size=[255,255]
screen=pygame.display.set_mode(screen_size)

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
            pos = pygame.mouse.get_pos()
            column_clicked = pos[0]//(width+margin)
            row_clicked = pos[1]//(height+margin)
            print("Row:",row_clicked,"Column:",column_clicked)
            grid[row_clicked][column_clicked] = 1

    # Set the screen background
    screen.fill(black)

    for row in range(10):
        for column in range(10):
            if grid[row][column] == 0:
                color=white
            else:
                color=green
            pygame.draw.rect(screen,color,[margin+(width+margin)*column,margin+(height+margin)*row,width,height])
                     
    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

