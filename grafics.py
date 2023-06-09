import settings
import pygame


def draw_lines(surface):
    for i in range(1, settings.SIZE):
        pygame.draw.line(surface,
                         pygame.Color(0, 0, 0),
                         (settings.WIDTH * i / settings.SIZE, 0),
                         (settings.WIDTH * i / settings.SIZE, settings.HEIGHT - 1),
                         10)

    for i in range(1, settings.SIZE):
        pygame.draw.line(surface,
                         pygame.Color(0, 0, 0),
                         (0, settings.HEIGHT * i / settings.SIZE),
                         (settings.WIDTH - 1, settings.HEIGHT * i / settings.SIZE),
                         10)


def draw_cross(surface: pygame.Surface, x_pos: int, y_pos: int):
    pygame.draw.line(surface,
                     pygame.Color(0, 0, 0),
                     (settings.WIDTH * x_pos / settings.SIZE, settings.HEIGHT * y_pos / settings.SIZE),
                     (settings.WIDTH * (x_pos + 1) / settings.SIZE, settings.HEIGHT * (y_pos + 1) / settings.SIZE),
                     5)

    pygame.draw.line(surface,
                     pygame.Color(0, 0, 0),
                     (settings.WIDTH * (x_pos + 1) / settings.SIZE, settings.HEIGHT * y_pos / settings.SIZE),
                     (settings.WIDTH * x_pos / settings.SIZE, settings.HEIGHT * (y_pos + 1) / settings.SIZE),
                     5)


def draw_circle(surface: pygame.Surface, x_pos: int, y_pos: int):
    radius = int(min(settings.WIDTH, settings.HEIGHT) / settings.SIZE / 2)

    pygame.draw.circle(surface,
                       pygame.Color(0, 0, 0),
                       (
                           settings.WIDTH * (x_pos + 0.5) / settings.SIZE,
                           settings.HEIGHT * (y_pos + 0.5) / settings.SIZE),
                       radius,
                       5)
