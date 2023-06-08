import pygame
import board
import settings

LEFT = 1
RIGHT = 3

def exit_handler(events):
    active = True
    for event in events:
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active = False
    return active


def gameloop(board_state):
    active = True

    while active:
        events = pygame.event.get()
        active = exit_handler(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                print("clicked")


def main():
    pygame.init()

    board_state = board.Board
    screen = pygame.display.set_mode((settings.HEIGHT, settings.WIDTH))

    gameloop(board_state)

    pygame.quit()



if __name__ == "__main__":
    main()
