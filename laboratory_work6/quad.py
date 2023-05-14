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
        self.points_dict = {"x1": x - size, "y1": y - size,
                            "x2": x - size, "y2": y + size,
                            "x3": x + size, "y3": y + size,
                            "x4": x + size, "y4": y - size}
        self.points = [x - size, y - size, x - size, y + size,
                       x + size, y + size, x + size, y - size]

    def __str__(self):
        return f"Quad({self._x}, {self._y})"

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
        self._x += dx
        self._y += dy
        # self.points[0] += dx
        # self.points[2] += dx
        # self.points[4] += dx
        # self.points[6] += dx
        for i in range(len(self.points)):
            if i % 2 == 0:
                self.points[i] += dx
            else:
                self.points[i] += dy
        # add logic to prevent go out canvas
        canvas.move(self._id, dx, dy)

    def update_points(self, x=-1, y=-1):
        for i in range(len(self.points)):
            if i in (0, 1, 2, 7):
                if i in (0, 2) and x != -1:
                    if x == 0:
                        self.points[i] = 0
                    else:
                        self.points[i] = x - 2 * self._size
                elif y != -1:
                    if y == 0:
                        self.points[i] = 0
                    else:
                        self.points[i] = y - self._size
            else:
                if i in (3, 5) and y != -1:
                    self.points[i] = y + self._size
                elif x != 0:
                    self.points[i] = x - self._size

    def check_collision(self, event, window_size):
        while True:
            dx, dy = 0, 0
            value = 5
            print(self._x, self._y)
            if self._x + self._size >= window_size["x"]:
                print(f"collision right need to move {window_size['x']}")
                self.update_points(window_size["x"])
                # dx = -(window_size["x"] - self._x)
                dx = -value
            if self._x - self._size <= 0:
                print(f"collision left need to move {0}")
                self.update_points(0)
                # dx = self._size - self._x
                dx = value
            if self._y + self._size >= window_size["y"] - 82:
                print(f"collision down need to move {window_size['y'] - 97}")
                self.update_points(y=window_size['y'] - 97)
                # dy = -(window_size["y"] - self._y - 97)
                dy = -value * 2
            if self._y - self._size <= 0:
                self.update_points(y=0)
                # dy = self._size - self._y
                dy = value
                print(f"collision up need to move {0}")
            if dx == dy == 0:
                break
            self.move(event.widget, dx, dy)
