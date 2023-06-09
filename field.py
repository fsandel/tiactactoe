class Field:
    def __init__(self, type: str = "EMPTY"):
        self.__type = type

    def __str__(self):
        return self.__type

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.__type == other.__type
        return False

    def toEmpty(self) -> None:
        self.__type = "EMPTY"

    def toCross(self) -> None:
        self.__type = "CROSS"

    def toCircle(self) -> None:
        self.__type = "CIRCLE"

    def getType(self) -> str:
        return self.__type


CIRCLE = Field("CIRCLE")
CROSS = Field("CROSS")
EMPTY = Field("EMPTY")
