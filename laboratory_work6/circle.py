R = 50


class Circle:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__r = R
        self.__id = -1
        self.selected = False

    def __str__(self):
        return f"Circle({self.__x}, {self.__y})"

    def get_id(self):
        return self.__id

    def draw(self, canvas):
        self.__id = canvas.create_oval(self.__x - self.__r,
                                       self.__y - self.__r,
                                       self.__x + self.__r,
                                       self.__y + self.__r)
        self.select(canvas)

    def select(self, canvas):
        self.selected = True
        canvas.itemconfigure(self.__id,
                             fill="#34eb95", tag="selected",
                             outline="#eb3434", width=5)

    def deselect(self, canvas):
        self.selected = False
        canvas.itemconfigure(self.__id, tag="not_selected", outline="")

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        if (event.x - self.__x) ** 2 + (event.y - self.__y) ** 2 <= self.__r ** 2:
            print("may select", event.x, event.y)
            # may select
            return True
        print("may draw", event.x, event.y)
        # may draw
        return False

    # methods that are decided to not realize or skip cos smth
    # def on_click(self, event):
    #     # logic of what to do: draw or select.....
    #     # if there is no drawed element
    #     if self.get_id() == -1:
    #         canvas = event.widget
    #         elems_around = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    #         for elem in elems_around:
    #             print(elem)
    #         self.draw(event.widget)
    #     else:
    #         if self.validate(event):
    #             print("may select")
    #             self.select(event.widget)
    #         else:
    #             print("may draw")
    #             self.draw(event.widget)
