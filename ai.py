import user
import field
import board
import random
import settings

MAX_DIFFICULTY = 0


class AI(user.User):
    def __init__(self, color: field.Field, difficulty: int):
        super().__init__(color)
        if difficulty > MAX_DIFFICULTY:
            raise Exception("It's over max difficulty")
        self.__difficulty = difficulty

    def getDifficulty(self):
        return self.__difficulty


class AI_easy(AI):
    def __init__(self, color):
        super().__init__(color, 0)

    def choose_next_place(self, board_state: board.Board):
        hit = False
        x_rand: int = 0
        y_rand: int = 0

        while not hit:
            x_rand = random.randint(0, settings.SIZE - 1)
            y_rand = random.randint(0, settings.SIZE - 1)
            print(f"x: {x_rand},   y: {y_rand}")
            if board_state[y_rand][x_rand] == field.EMPTY:
                hit = True

        board_state[y_rand][x_rand] = self.getColor()
        return x_rand, y_rand
