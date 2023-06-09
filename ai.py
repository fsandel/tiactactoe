import user
import field

MAX_DIFFICULTY = 0


class AI(user.User):
    def __init__(self, color: field.Field, difficulty: int):
        super().__init__(color)
        if difficulty > MAX_DIFFICULTY:
            raise Exception("It's over max difficulty")
        self.__difficulty = difficulty
