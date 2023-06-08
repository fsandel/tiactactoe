import pygame
import board

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

b = board.Board(3)
# print(b)
b[1][1].toCross()
# b.flushBoard()
print(b[1][1])
