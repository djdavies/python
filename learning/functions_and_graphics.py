# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

# Import a library of functions called 'pygame'
import pygame

# --- Function for a snowman ---
# Define a function that will draw a snowman at a certain location
def draw_snowman(screen,x,y):
    pygame.draw.ellipse(screen,white,[35+x,0+y,25,25])
    pygame.draw.ellipse(screen,white,[23+x,20+y,50,50])
    pygame.draw.ellipse(screen,white,[0+x,65+y,100,100])
    
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255,255,255]
blue = [ 0, 0,255]
green = [ 0,255, 0]
red = [255, 0, 0]

pi=3.141592653

# Set the height and width of the screen
size=[400,500]
screen=pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done=False
clock = pygame.time.Clock()

while done==False:

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(black)

    # Snowman in upper left
    draw_snowman(screen,10,10)
    
    # Snowman in upper right
    draw_snowman(screen,300,10)
    
    # Snowman in lower left
    draw_snowman(screen,10,300)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit ()

