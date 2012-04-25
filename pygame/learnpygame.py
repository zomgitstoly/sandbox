import pygame
import random


#initializes pygame
pygame.init()

#setting some colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

pi=3.141592653
#Opens up a new window of size
size=[600,600]
screen = pygame.display.set_mode(size)
#sets the caption for the window
pygame.display.set_caption("Learning")
done = False
rect_x = 600
clock=pygame.time.Clock()
rectangle = []
for i in range(6):
	ypos = random.randrange(600)
	a = 600,ypos
	rectangle.append(a)
while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

	screen.fill(white)
	# Draw on the screen a green line from (0,0) to (100,100)
	# that is 5 pixels wide.	
	pygame.draw.line(screen,green,[0,0],[100,100],10)
	for i in range(6):
		pygame.draw.rect(screen,red,[rectangle[i][0],rectangle[i][1],10,10])
		rectangle[i] = rectangle[i][0]-10,rectangle[i][1]
	#for i in range(6):
	#	rectangle[i] = rectangle[i].move(-10,0)	
	#limits maximum FPS
	clock.tick(30)
	pygame.display.flip() #Updates the screen
#Finally for real closes the program
pygame.quit()

