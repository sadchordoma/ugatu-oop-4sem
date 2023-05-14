from figure import Figure


class Triangle(Figure):
    def __init__(self, x: int, y: int, size: int, color: str):
        super().__init__(x, y, size, color)
        # x2,y2   x3,y3
        # --------------
        # |            |
        # |            |
        # --------------
        # x1,y1    x4,y4
        self.points_dict = {"x1": x - size, "y1": y - size,
                       "x2": x - size, "y2": y + size,
                       "x3": x + size, "y3": y + size,
                       "x4": x + size, "y4": y - size}
        self.points = [x - size, y - size, x - size, y + size,
                       x + size, y + size, x + size, y - size]

    def __str__(self):
        return f"Quad({self._x}, {self._y})"

    def get_id(self):
        return self._id

    def set_color(self, color: str):
        self.color = color

    def select(self, canvas):
        self.selected = True
        canvas.itemconfigure(self._id,
                             fill=self.color, tag="selected",
                             outline="#eb3434", width=5)

    def deselect(self, canvas):
        self.selected = False
        canvas.itemconfigure(self._id, tag="not_selected", outline="")

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        # if self.points_dict["x1"] <= event.x <= self.points_dict["x4"] and self.points_dict["y1"] <= event.y <=
        #         self.points_dict["y3"]:
        if self.points[0] <= event.x <= self.points[4] and self.points[1] <= event.y <= self.points[3]:
            # print("may select", event.x, event.y)
            # may select
            return True
            # print("may draw", event.x, event.y)
            # may draw
        return False

    def resize(self, canvas, size: int):
        if self._size > size:
            diff = -(self._size - size)
        else:
            diff = size - self._size

        self._size = size
        self._x += diff
        self._y += diff
        for i in range(len(self.points)):
            if i in (0, 1, 2, 7):
                self.points[i] -= diff
            else:
                self.points[i] += diff
        canvas.coords(self._id, self.points)

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        self.select(canvas)

    def move(self, canvas, dx=0, dy=0):

        # add logic to prevent go out canvas
        canvas.move(self._id, dx, dy)

