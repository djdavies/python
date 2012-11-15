# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (  50,  50, 255)
green    = (   0, 255,   0)
dkgreen  = (   0, 100,   0)
red      = ( 255,   0,   0)
purple   = (0xBF,0x0F,0xB5)
brown    = (0x55,0x33,0x00)

# Function to draw the background
def draw_background(screen):
    # Set the screen background
    screen.fill(white)

def draw_item(screen,x,y):
    pygame.draw.rect(screen,green,[0+x,0+y,30,10],0)
    pygame.draw.circle(screen,black,[15+x,5+y],7,0)
    
pygame.init()

       
screen = pygame.display.set_mode((640, 480))

# Current position
x_coord=10
y_coord=10

# Count the joysticks the computer has
joystick_count=pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print ("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
            
clock = pygame.time.Clock()

done=False
while done==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            
    # As long as there is a joystick
    if joystick_count != 0:
    
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos= my_joystick.get_axis(0)
        vert_axis_pos= my_joystick.get_axis(1)   
        
        # Move x according to the axis. We multiply by 10 to speed up the movement.
        x_coord=int(x_coord+horiz_axis_pos*10)
        y_coord=int(y_coord+vert_axis_pos*10)

    
    draw_background(screen)

    # Draw the item at the proper coordinates
    draw_item(screen,x_coord,y_coord)       
    
    pygame.display.flip()
    clock.tick(40)
    
pygame.quit ()
