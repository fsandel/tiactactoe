import board
import field
import pygame
import grafics


class User:
    def __init__(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def draw(self, surface: pygame.Surface, x_pos: int, y_pos: int):
        if self.__color == field.CIRCLE:
            grafics.draw_circle(surface, x_pos, y_pos)
        if self.__color == field.CROSS:
            grafics.draw_cross(surface, x_pos, y_pos)


class Player(User):
    def setField(self, board_state: board.Board, x, y):
        if board_state[y][x] == field.EMPTY:
            board_state.setField(self.getColor(), x, y)
