import time

R = 25


class Circle:
    def __init__(self, x: int, y: int, r: int, color: str):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__id = -1
        self.color = color
        self.selected = False

    def __str__(self):
        return f"Circle({self.__x}, {self.__y})"

    def get_id(self):
        return self.__id

    def set_color(self, color: str):
        self.color = color

    def select(self, canvas):
        self.selected = True
        canvas.itemconfigure(self.__id,
                             fill=self.color, tag="selected",
                             outline="#eb3434", width=5)

    def deselect(self, canvas):
        self.selected = False
        canvas.itemconfigure(self.__id, tag="not_selected", outline="")

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        if (event.x - self.__x) ** 2 + (event.y - self.__y) ** 2 <= self.__r ** 2:
            # print("may select", event.x, event.y)
            # may select
            return True
            # print("may draw", event.x, event.y)
            # may draw
        return False

    def resize(self, canvas, r: int):
        self.__r = r
        canvas.coords(self.__id, self.__x - self.__r, self.__y - self.__r,
                      self.__x + self.__r, self.__y + self.__r)

    def draw(self, canvas):
        self.__id = canvas.create_oval(self.__x - self.__r,
                                       self.__y - self.__r,
                                       self.__x + self.__r,
                                       self.__y + self.__r)
        self.select(canvas)

    def move(self, canvas, dx=0, dy=0):
        self.__x += dx
        self.__y += dy
        # add logic to prevent go out canvas
        canvas.move(self.__id, dx, dy)

    # collision detect?????
    # def check_collision(self, event, window_size):
    #     if event.x + self.__r >= window_size["x"]:
    #         print("collision right")
    #     elif event.x - self.__r <= 0:
    #         print("collision left")
    #     elif event.y + self.__r >= window_size["y"] - 80:
    #         print("collision down")
    #     elif event.y - self.__r <= 0:
    #         print("collision up")
    def check_collision(self, event, window_size):
        while True:
            dx, dy = 0, 0
            value = 5
            print(self.__x, self.__y)
            if self.__x + self.__r >= window_size["x"]:
                print("collision right")
                dx = -value
            elif self.__x - self.__r <= 0:
                print("collision left")
                dx = value
            elif self.__y + self.__r >= window_size["y"] - 82:
                print("collision down")
                dy = -value - value
            elif self.__y - self.__r <= 0:
                dy = value
                print("collision up")
            print(dx, dy)
            if dx == dy == 0:
                return True
            self.move(event.widget, dx, dy)
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
