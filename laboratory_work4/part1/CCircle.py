class CCircle:
    def __init__(self, x:int, y:int):
        self.__x = x
        self.__y = y
        self.__diameter = 5  # const

    def __str__(self):
        return f"{self.__x}, {self.__y} with r = {self.__diameter}"
