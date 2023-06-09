import pygame
import board
import settings
import user
import field
import grafics
import ai

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


def gameloop(surface, board_state):
    active = True

    x_pos = 0
    y_pos = 0

    player = user.Player(field.CIRCLE)
    ai_player = ai.AI_easy(field.CROSS)

    while active:

        events = pygame.event.get()
        active = exit_handler(events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x_pos = int(pygame.mouse.get_pos()[0] * settings.SIZE / settings.WIDTH)
                y_pos = int(pygame.mouse.get_pos()[1] * settings.SIZE / settings.HEIGHT)
                player.setField(board_state, x_pos, y_pos)
                player.draw(surface, x_pos, y_pos)
                ai_player.draw(surface, *ai_player.choose_next_place(board_state))
                print(board_state)

        pygame.display.flip()


def main():
    pygame.init()

    board_state = board.Board(settings.SIZE)
    surface = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    surface.fill((255, 255, 255))
    grafics.draw_lines(surface)

    gameloop(surface, board_state)

    pygame.quit()


if __name__ == "__main__":
    main()
