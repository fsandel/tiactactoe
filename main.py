import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))

active = True

while active:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				active = False

pygame.quit()