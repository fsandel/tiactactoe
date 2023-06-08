
class Field:
    def __init__(self):
        self.__type = "EMPTY"

    def __str__(self):
        return self.__type

    def toEmpty(self) -> None:
        self.__type = "EMPTY"

    def toCross(self) -> None:
        self.__type = "CROSS"

    def toCircle(self) -> None:
        self.__type = "CIRCLE"

    def getType(self) -> str:
        return self.__type
