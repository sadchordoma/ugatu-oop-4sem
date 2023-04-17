R = 50


class Circle:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__r = R
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

    def deselect(self, canvas):
        canvas.itemconfigure(self.__id, tag="not_selected", outline="")

    def validation(self, event):
        if (event.x - self.__x) ** 2 + (event.y - self.__y) ** 2 <= R ** 2:
            # select
            return 1, self.__id
        # draw
        return 0, -1

    @staticmethod
    def select_circles_area(event, circles_in_area, all_circles, canvas):
        for circle in circles_in_area:
            existed_circle = all_circles[circle]
            is_element_here, id_elem = existed_circle.validation(event)
            if is_element_here:
                existed_circle = all_circles[id_elem]
                existed_circle.select(canvas)