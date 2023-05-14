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
            # may select
            return True
        # may draw
        return False

    def resize(self, canvas, size: int, window_size=None):
        diff = size - self._size
        self._size = size
        self.update_points(self._x + diff, self._y + diff)

        canvas.coords(self._id, self.points)
        self.check_collision(canvas, window_size)

    def draw(self, canvas):
        self._id = canvas.create_polygon(self.points)
        self.select(canvas)

    def update_points(self, x, y):
        self._x = x
        self._y = y
        self.points = [self._x, self._y - self._size,
                       self._x + self._size, self._y + self._size,
                       self._x - self._size, self._y + self._size]

    def move(self, canvas, dx=0, dy=0):
        self.update_points(self._x + dx, self._y + dy)
        # add logic to prevent go out canvas
        canvas.move(self._id, dx, dy)

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
