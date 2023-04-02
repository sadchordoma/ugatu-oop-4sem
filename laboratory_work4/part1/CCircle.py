R = 25
class CCircle:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__r = R  # const
        self.__id = -1

    def __str__(self):
        return f"({self.__x},{self.__y}),r={self.__r},id={self.__id}"

    def get_id(self):
        return self.__id

    @staticmethod
    def create_circle(x, y, r, canvas, **kwargs):
        return canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    # is to skip
    def validation(self, event, canvas):
        found_closest = canvas.find_closest(event.x, event.y, self.__r)
        if not found_closest:
            return False
        else:
            cords = canvas.coords(found_closest[0])
            x, y = cords[:2]  # get first 2 cords from (x1, y1, x2, y2)
            x += self.__r
            y += self.__r
            if abs(event.x - x) < self.__r and abs(event.y - y) < self.__r:
                print("skipped")
                return found_closest
            # else
            return False

    def draw(self, event, canvas):
        new_circle = self.create_circle(
            event.x, event.y, self.__r, canvas,
            fill="#03a5fc", outline="red", width=3, tag="selected")
        self.__id = new_circle
        # print(f"created with {event.x}, {event.y}")

    def select_or_draw(self, event, canvas):
        found_closest = self.validation(event, canvas)
        if not found_closest:
            self.draw(event, canvas)
        else:
            self.select(found_closest[0])

    def select(self, found_closest, canvas):
        if canvas.itemcget(found_closest, "outline") == "red":
            canvas.itemconfig(found_closest, outline="", tag="not_selected")
        else:
            canvas.itemconfig(found_closest, outline="", tag="selected")