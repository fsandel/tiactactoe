import field


class Board:

    def __init__(self, size):
        self.__size = size
        self.__field = [[field.Field()] * size] * size

    def __str__(self):
        s = ""
        for row in self.__field:
            for f in row:
                s += f.getType() + " "
            s += "\n"
        return s

    def __getitem__(self, item):
        return self.__field[item]

    def __setitem__(self, key, value):
        self.__field[key] = value

    def flushBoard(self):
        for line in self.__field:
            for f in line:
                f.toEmpty()
