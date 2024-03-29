from figure import Figure


class Circle(Figure):
    def __init__(self, x: int, y: int, r: int, color: str):
        super().__init__(x, y, r, color)
        self._r = r

    def __str__(self):
        return f"Circle({self._x}, {self._y})"

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        if (event.x - self._x) ** 2 + (event.y - self._y) ** 2 <= self._r ** 2:
            # may select
            return True
            # may draw
        return False

    def resize(self, canvas, r: int, window_size=None):
        self._r = r
        canvas.coords(self._id, self._x - self._r, self._y - self._r,
                      self._x + self._r, self._y + self._r)
        self.check_collision(canvas, window_size)

    def draw(self, canvas):
        self._id = canvas.create_oval(self._x - self._r,
                                      self._y - self._r,
                                      self._x + self._r,
                                      self._y + self._r)
        self.select(canvas)

    # def move(self, canvas, dx=0, dy=0, mode="move"):
    #     self._x += dx
    #     self._y += dy
    #     canvas.move(self._id, dx, dy)

    def update_points(self, dx, dy, mode="move"):
        if mode == "move":
            self._x += dx
            self._y += dy

    def move_to(self, canvas, x, y):
        self._x = x
        self._y = y
        canvas.coords(self._id, self._x - self._r, self._y - self._r,
                      self._x + self._r, self._y + self._r)

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
            if self._x - self._r < 0:
                print("collision left")
                # self._x = self._r
                self.move_to(canvas, self._r, self._y)
            if self._x + self._r > window_x:
                print("collision right")
                # self._x = window_x - self._r
                self.move_to(canvas, window_x - self._r, self._y)
            if self._y - self._r < 0:
                print("collision up")
                # self.y = self._r + 2
                self.move_to(canvas, self._x, self._r + self.magic_add_size)
            if self._y + self._r > window_y - self.magic_size:
                print("collision down")
                # 87 iz za togo 4to coordinati berutsya otnositelno?
                # self._y = window_y - 87 - self._r
                self.move_to(canvas, self._x, window_y - self.magic_size - self._r)
