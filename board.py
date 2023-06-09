import field
import settings


class Board:

    def __init__(self, size):
        self.__size = size
        self.__field = [[field.EMPTY for i in range(size)] for j in range(size)]

    def __str__(self):
        s = ""
        for row in self.__field:
            for r in row:
                s += r.getType() + " "
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

    def getEmptyFields(self) -> int:
        empty_fields: int = 0

        for row in self.__field:
            for r in row:
                if r == field.EMPTY:
                    empty_fields += 1

        return empty_fields

    def __checkRows(self) -> field.Field:
        for row in self.__field:
            if row == [field.CIRCLE] * settings.SIZE:
                return field.CIRCLE
            if row == [field.CROSS] * settings.SIZE:
                return field.CROSS
        return field.EMPTY

    def __checkColumns(self) -> field.Field:
        for column in range(settings.SIZE):
            sub_list = []
            for row in range(settings.SIZE):
                sub_list.append(self[row][column])
            if sub_list == [field.CROSS] * settings.SIZE:
                return field.CROSS
            if sub_list == [field.CIRCLE] * settings.SIZE:
                return field.CIRCLE

        return field.EMPTY

    def __checkDiagonals(self) -> field.Field:
        sub_list = []
        for i in range(settings.SIZE):
            sub_list.append(self[i][i])
        if sub_list == [field.CIRCLE] * settings.SIZE:
            return field.CIRCLE
        if sub_list == [field.CROSS] * settings.SIZE:
            return field.CROSS

        sub_list = []
        for i in range(settings.SIZE):
            sub_list.append(self[settings.SIZE - 1 - i][i])
        if sub_list == [field.CIRCLE] * settings.SIZE:
            return field.CIRCLE
        if sub_list == [field.CROSS] * settings.SIZE:
            return field.CROSS

        return field.EMPTY

    def checkWinner(self) -> field.Field:
        if self.__checkRows() == field.CROSS:
            return field.CROSS
        if self.__checkRows() == field.CIRCLE:
            return field.CIRCLE

        if self.__checkColumns() == field.CROSS:
            return field.CROSS
        if self.__checkColumns() == field.CIRCLE:
            return field.CIRCLE

        if self.__checkDiagonals() == field.CROSS:
            return field.CROSS
        if self.__checkDiagonals() == field.CIRCLE:
            return field.CIRCLE

        return field.EMPTY
