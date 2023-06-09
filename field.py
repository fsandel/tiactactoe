EMPTY = "EMPTY"
CROSS = "CROSS"
CIRCLE = "CIRCLE"


class Field:
    def __init__(self, type=EMPTY):
        self.__type = type

    def __str__(self):
        return self.__type

    def toEmpty(self) -> None:
        self.__type = EMPTY

    def toCross(self) -> None:
        self.__type = CROSS

    def toCircle(self) -> None:
        self.__type = CIRCLE

    def getType(self) -> str:
        return self.__type
