import pygame

black = [0,0,0]
white = [255,255,255]
blue = [0,0,255]
green = [0,255,0]
red = [255,0,0]

pygame.init()

size = [700,500]
screen = pygame.display.set_mode(size)
screen.fill(black)
pygame.display.set_caption("Template")
clock=pygame.time.Clock()
background = pygame.image.load("sky.JPG").convert()
screen.blit(background, [0,0])
done = False

rect_x = 50
rect_y = 50

class Block(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(color)

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
	screen.blit(background, [0,0])		
	clock.tick(20)
	pygame.draw.rect(screen,white,[rect_x,rect_y,50,50])
	rect_x += 1
	rect_y += 1

	pygame.display.flip()
pygame.quit()
