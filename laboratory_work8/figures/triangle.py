from .figure import Figure


class Triangle(Figure):
    def __init__(self, x: int, y: int, size: int, color: str, selected: bool):
        super().__init__(x, y, size, color, selected)
        #     x3,y3
        #      /\
        #      --
        # x1,y1  x2,y2

        # x1, y1, x2,y2, x3,y3
        self.points = [x - size, y + size, x + size, y + size, x, y - size]

    def __str__(self):
        return "Triangle"

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        a = (self.points[0] - event.x) * (self.points[3] - self.points[1]) - (self.points[2] - self.points[0]) * (
                self.points[1] - event.y)
        b = (self.points[2] - event.x) * (self.points[5] - self.points[3]) - (self.points[4] - self.points[2]) * (
                self.points[3] - event.y)
        c = (self.points[4] - event.x) * (self.points[1] - self.points[5]) - (self.points[0] - self.points[4]) * (
                self.points[5] - event.y)
        if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
            print("may select")
            return True
        print("may draw")
        return False

    def resize(self, canvas, size: int, window_size=None):
        diff = size - self._size
        self._size = size
        self.update_points(self._x + diff, self._y + diff, "to")
        canvas.coords(self._id, self.points)
        self.fix_collision(canvas, window_size)

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        canvas.itemconfigure(self._id, fill=self._color, outline="")
        if self.selected:
            self.select(canvas)

    def update_points(self, dx, dy, mode="move"):
        if mode == "move":
            self._x += dx
            self._y += dy
            self.points = [self._x - self._size, self._y + self._size,
                           self._x + self._size, self._y + self._size,
                           self._x, self._y - self._size]
        elif mode == "to":
            self._x = dx
            self._y = dy
            self.points = [self._x - self._size, self._y + self._size,
                           self._x + self._size, self._y + self._size,
                           self._x, self._y - self._size]

    def move_to(self, canvas, x, y):
        dx, dy = x - self._x, y - self._y
        # self.update_points(dx, dy)
        self.move(canvas, dx, dy, "move")
