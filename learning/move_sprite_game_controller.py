# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)

# This class represents the ball        
# It derives from the "Sprite" class in Pygame
class Ball(pygame.sprite.Sprite):

    joystick_count = 0
    
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 

        # Variables to hold the height and width of the block
        width=20
        height=15

        # Create an image of the ball, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(black)

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
        # Set initial position of sprite to 100,100
        self.rect.left=100
        self.rect.top=100
        
        # Count the joysticks the computer has
        self.joystick_count=pygame.joystick.get_count()
        if self.joystick_count == 0:
            # No joysticks!
            print ("Error, I didn't find any joysticks.")
        else:
            # Use joystick #0 and initialize it
            self.my_joystick = pygame.joystick.Joystick(0)
            self.my_joystick.init()
        

    # Update the position of the ball
    def update(self):
        # As long as there is a joystick
        if self.joystick_count != 0:
        
            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos= self.my_joystick.get_axis(0)
            vert_axis_pos= self.my_joystick.get_axis(1)   
            
            # Move x according to the axis. We multiply by 10 to speed up the movement.
            self.rect.left=self.rect.left+horiz_axis_pos*10
            self.rect.top=self.rect.top+vert_axis_pos*10


pygame.init()
    
# Set the height and width of the screen
size=[700,500]
screen=pygame.display.set_mode(size)

#Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# This is a list of 'sprites.' Each ball in the program (there is only 1) is
# added to this list. The list is managed by a class called 'RenderPlain.'
balls = pygame.sprite.RenderPlain()

# This represents the ball controlled by the player
ball = Ball()

# Add the ball to the list of player-controlled objects
balls.add(ball)

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Clear the screen
    screen.fill(white)

    # Update the position of the ball (using the mouse) and draw the ball
    ball.update()
    balls.draw(screen)

    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit ()
