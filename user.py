import board
import field


class User:
    def __init__(self, color):
        self.__color = field.Field(color)

    def getColor(self):
        return self.__color


class Player(User):
    def setField(self, board_state: board.Board, x, y):
        if board_state[y][x].getType() == field.EMPTY:
            board_state.setField(self.getColor(), x, y)
