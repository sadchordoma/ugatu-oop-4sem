from figure import Figure


class Quad(Figure):
    def __init__(self, x: int, y: int, size: int, color: str):
        super().__init__(x, y, size, color)
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
        return f"Quad({self._x}, {self._y})"

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
        self.check_collision(canvas, window_size)

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        self.select(canvas)

    # def move(self, canvas, dx=0, dy=0, mode="0"):
    #     self.update_points(dx, dy, "move")
    #     canvas.move(self._id, dx, dy)

    def update_points(self, x, y, mode="move"):
        if mode == "0":
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
        self.update_points(x, y, "0")
        canvas.coords(self._id, self.points)
        # self.move(canvas, x, y, "0")

    def check_collision(self, canvas, window_size, just_check=False):
        window_x = window_size["x"]
        window_y = window_size["y"]

        if just_check:
            if self._x - self._size < 0:
                return True
            if self._x + self._size > window_x:
                return True
            if self._y - self._size < 0:
                return True
            if self._y + self._size > window_y - self.magic_size:
                return True
            return False
        else:
            if self._x - self._size <= 0:
                print("collision left")
                # self._x = self._size
                self.move_to(canvas, self._size + self.magic_add_size, self._y)
            if self._x + self._size >= window_x:
                print("collision right")
                # self._x = window_x - self._r
                self.move_to(canvas, window_x - self._size - self.magic_add_size, self._y)
            if self._y - self._size <= 0:
                print("collision up")
                # self.y = self._r + 2
                self.move_to(canvas, self._x, self._size + self.magic_add_size)
            if self._y + self._size >= window_y - self.magic_size:
                print("collision down")
                # 87 iz za togo 4to coordinati berutsya otnositelno?
                # self._y = window_y - 87 - self._r
                self.move_to(canvas, self._x, window_y - self.magic_size - self._size)
