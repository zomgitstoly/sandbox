import pygame
pygame.init()
black = [0,0,0]
white = [255,255,255]
blue = [0,0,255]
green = [0,255,0]
red = [255,0,0]

size = [400,400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Testing 1,2,3")
font = pygame.font.Font(None,25)

done=False
clock = pygame.time.Clock()


while done == False:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
			
	screen.fill(white)
	pygame.draw.line(screen,green,[0,0],[100,100],5)
	text = font.render("hello", True,green)
	screen.blit(text,[250,250])
	y_offset = 0
	while y_offset < 100:
		pygame.draw.line(screen,red,[0,10+y_offset], [100,110+y_offset],5)
		y_offset = y_offset+10
	pygame.display.flip()
pygame.quit()
