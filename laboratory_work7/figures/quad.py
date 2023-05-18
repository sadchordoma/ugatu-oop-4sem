from .figure import Figure


class Quad(Figure):
    def __init__(self, x: int, y: int, size: int, color: str, selected: bool):
        super().__init__(x, y, size, color, selected)
        # x2,y2   x3,y3
        # --------------
        # |            |
        # |            |
        # --------------
        # x1,y1    x4,y4

        # x1,y1, x2,y2, x3,y3, x4,y4
        self.points = [x - size, y - size, x - size, y + size,
                       x + size, y + size, x + size, y - size]

    def __str__(self):
        return "Quad"

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        # if x1 <= e.x <= x4 and y1 <= e.y <= y3:
        if self.points[0] <= event.x <= self.points[4] and self.points[1] <= event.y <= self.points[3]:
            # may select
            return True
            # may draw
        return False

    def resize(self, canvas, size: int, window_size=None):
        diff = size - self._size
        self._size = size
        self.update_points(diff, diff, "resize")
        canvas.coords(self._id, self.points)
        self.fix_collision(canvas, window_size)

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        canvas.itemconfigure(self._id, fill=self._color, outline="")
        if self.selected:
            self.select(canvas)

    def update_points(self, x, y, mode="move"):
        if mode == "to":
            self._x = x
            self._y = y
            self.points = [self._x - self._size, self._y - self._size,
                           self._x - self._size, self._y + self._size,
                           self._x + self._size, self._y + self._size,
                           self._x + self._size, self._y - self._size]

        elif mode == "move":
            self._x += x
            self._y += y
            for i in range(len(self.points)):
                if i % 2 == 0:
                    self.points[i] += x
                else:
                    self.points[i] += y
        elif mode == "resize":
            # diff = x = y
            diff = x
            self._x += diff
            self._y += diff
            self.points = [self._x - self._size, self._y - self._size,
                           self._x - self._size, self._y + self._size,
                           self._x + self._size, self._y + self._size,
                           self._x + self._size, self._y - self._size]

    def move_to(self, canvas, x, y):
        dx, dy = x - self._x, y - self._y
        self.update_points(x, y, "to")
        canvas.coords(self._id, self.points)
        # self.move(canvas, x, y, "0")
