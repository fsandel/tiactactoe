import field


class Row:
    def __init__(self, size):
        self.__row = [field.Field()] * size

    def __str__(self):
        s = ""
        for f in self.__row:
            s += f.getType()
        return s

    def __getitem__(self, item):
        return self.__row[item]

    def __setitem__(self, key, value):
        self.__row[key] = value

    def getRow(self):
        s = ""
        for f in self.__row:
            s += f.getType() + " "
        return s


class Board:

    def __init__(self, size):
        self.__size = size
        self.__field = [Row(size)] * size

    def __str__(self):
        s = ""
        for row in self.__field:
            s += row.getRow() + "\n"
        return s

    def __getitem__(self, item):
        return self.__field[item]

    def __setitem__(self, key, value):
        self.__field[key] = value

    def flushBoard(self):
        for line in self.__field:
            for f in line:
                f.toEmpty()
