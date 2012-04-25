# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

pygame.init()
 

size=[700,500]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


done=False
rect_x = 50

clock=pygame.time.Clock()

while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(black)

    # Limit to 20 frames per second
    clock.tick(20)
	#pygame.draw.rect(screen,white,[rect_x,50,50,50])
	rect_x += 1
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()

