import field


class Board:

    def __init__(self, size):
        self.__size = size
        self.__field = [[field.Field() for i in range(size)] for j in range(size)]

    def __str__(self):
        s = ""
        for row in self.__field:
            for r in row:
                s += r.__str__() + " "
            s += "\n"
        return s

    def __getitem__(self, item):
        return self.__field[item]

    def __setitem__(self, key, value):
        self.__field[key] = value

    def setField(self, f, x, y):
        self.__field[y][x] = f

    def flushBoard(self):
        for line in self.__field:
            for f in line:
                f.toEmpty()
