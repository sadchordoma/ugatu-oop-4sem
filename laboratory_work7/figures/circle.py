from .figure import Figure


class Circle(Figure):
    def __init__(self, x: int, y: int, r: int, color: str, selected: bool):
        super().__init__(x, y, r, color, selected)
        self._r = r

    def __str__(self):
        return "Circle"

    # validate whether there is an element on event.x && event.y or no
    def validate_select(self, event):
        if (event.x - self._x) ** 2 + (event.y - self._y) ** 2 <= self._r ** 2:
            # may select
            return True
            # may draw
        return False

    def resize(self, canvas, r: int, window_size=None):
        self._r = r
        self._size = r
        canvas.coords(self._id, self._x - self._r, self._y - self._r,
                      self._x + self._r, self._y + self._r)
        self.fix_collision(canvas, window_size)

    def draw(self, canvas):
        # need this if was loaded from file

        self._id = canvas.create_oval(self._x - self._r,
                                      self._y - self._r,
                                      self._x + self._r,
                                      self._y + self._r)
        canvas.itemconfigure(self._id, fill=self._color, outline="")
        if self.selected:
            self.select(canvas)

    def update_points(self, dx, dy, mode="move"):
        if mode == "move":
            self._x += dx
            self._y += dy
        elif mode == "to":
            self._x = dx
            self._y = dy

    def move_to(self, canvas, x, y):
        self._x = x
        self._y = y
        canvas.coords(self._id, self._x - self._r, self._y - self._r,
                      self._x + self._r, self._y + self._r)

    def load(self, file, **kwargs):
        s = file.readline()
        print("atr for figure", s)
        tuple_attr = s.split(",")
        self._x = int(tuple_attr[0])
        self._y = int(tuple_attr[1])
        self._size = int(tuple_attr[2])
        self._r = self._size
        self._color = tuple_attr[3].strip()
        self._selected = eval(tuple_attr[4])
