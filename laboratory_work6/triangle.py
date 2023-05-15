import time

from figure import Figure


class Triangle(Figure):
    def __init__(self, x: int, y: int, size: int, color: str):
        super().__init__(x, y, size, color)
        #     x3,y3
        #      /\
        #      --
        # x1,y1  x2,y2

        # x1, y1, x2,y2, x3,y3
        self.points = [x - size, y + size, x + size, y + size, x, y - size]

    def __str__(self):
        return f"Triangle({self._x}, {self._y})"

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
        self.update_points(self._x + diff, self._y + diff, "0")
        canvas.coords(self._id, self.points)

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        self.select(canvas)

    def update_points(self, dx, dy, mode="move"):
        if mode == "move":
            self._x += dx
            self._y += dy
            self.points = [self._x - self._size, self._y + self._size,
                           self._x + self._size, self._y + self._size,
                           self._x, self._y - self._size]
        elif mode == "0":
            self._x = dx
            self._y = dy
            self.points = [self._x - self._size, self._y + self._size,
                           self._x + self._size, self._y + self._size,
                           self._x, self._y - self._size]
    # def move(self, canvas, dx=0, dy=0, mode="move"):
    #     self.update_points(self._x + dx, self._y + dy)
    # canvas.move(self._id, dx, dy)

    def move_to(self, canvas, x, y):
        dx, dy = x - self._x, y - self._y
        self.update_points(dx, dy)
        self.move(self._id, dx, dy)

    def check_collision(self, canvas, window_size):
        window_x = window_size["x"]
        window_y = window_size["y"]
        if self._x - self._size <= 0:
            print("collision left")
            # self._x = self._r
            self.move_to(canvas, self._size, self._y)
        if self._x + self._size >= window_x:
            print("collision right")
            # self._x = window_x - self._r
            self.move_to(canvas, window_x - self._size, self._y)
        if self._y - self._size <= 0:
            print("collision up")
            # self.y = self._r + 2
            self.move_to(canvas, self._x, self._size + self.magic_add_size)
        if self._y + self._size >= window_y - self.magic_size:
            print("collision down")
            # 87 iz za togo 4to coordinati berutsya otnositelno?
            # self._y = window_y - 87 - self._r
            self.move_to(canvas, self._x, window_y - self.magic_size - self._size)
