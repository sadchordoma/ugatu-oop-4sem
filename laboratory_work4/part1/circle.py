R = 50


class Circle:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__r = 50
        self.__id = -1

    def get_id(self):
        return self.__id

    def draw(self, canvas):
        self.__id = canvas.create_oval(
            self.__x - self.__r, self.__y - self.__r,
            self.__x + self.__r, self.__y + self.__r
        )

    def select(self, canvas):
        canvas.itemconfigure(self.__id, fill="#34eb95", tag="selected", outline="#eb3434", width=5)
