import time

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
        print(event.x, event.y, self._x, self._y)
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

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        self.select(canvas)

    def move(self, canvas, dx=0, dy=0):
        self.update_points(dx, dy, "move")
        canvas.coords(self._id, self.points)

    def update_points(self, x, y, mode="0"):
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
            for i in range(len(self.points)):
                if i in (0, 1, 2, 7):
                    self.points[i] -= diff
                else:
                    self.points[i] += diff

    def move_to(self, canvas, x, y):
        self.update_points(x, y)
        canvas.coords(self._id, self.points)

    def check_collision(self, event, window_size, just_check=False):
        window_x = window_size["x"]
        window_y = window_size["y"]
        if just_check:
            if self._x - self._size < 0:
                print("collision left")
                return True
            if self._x + self._size > window_x:
                print("collision right")
                return True
            if self._y - self._size < 0:
                print("collision up")
                return True
            if self._y + self._size > window_y - 87:
                print("collision down")
                return True
        else:
            if self._x - self._size < 0:
                print("collision left")
                # self._x = self._r
                self.move_to(event, self._size, self._y)
            if self._x + self._size > window_x:
                print("collision right")
                # self._x = window_x - self._r
                self.move_to(event, window_x - self._size, self._y)
            if self._y - self._size < 0:
                print("collision up")
                # self.y = self._r + 2
                self.move_to(event, self._x, self._size + 2)
            if self._y + self._size > window_y - 87:
                print("collision down")
                # 87 iz za togo 4to coordinati berutsya otnositelno?
                # self._y = window_y - 87 - self._r
                self.move_to(event, self._x, window_y - 87 - self._size)
