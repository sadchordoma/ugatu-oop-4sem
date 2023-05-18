from abc import ABC, abstractmethod
from settings import MAGIC_CONST, MAGIC_ADD_CONST


class Figure(ABC):
    def __init__(self, x: int, y: int, size: int, color: str, selected=False):
        self._x = x
        self._y = y
        self._size = size
        self._id = -1
        self._color = color
        self._selected = selected

    @abstractmethod
    def __str__(self):
        pass

    @property
    def selected(self):
        return self._selected

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _id):
        self._id = _id

    @property
    def color(self):
        return self._color

    def set_color(self, canvas, color: str):
        self._color = color
        canvas.itemconfigure(self._id, outline=self._color)

    # validate whether there is an element on event.x && event.y or no
    @abstractmethod
    def validate_select(self, event):
        pass

    @abstractmethod
    def resize(self, canvas, size: int):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass

    @abstractmethod
    def update_points(self, x, y, mode="move"):
        pass

    def select(self, canvas):
        self._selected = True
        canvas.itemconfigure(self._id, tag="selected",fill=self.color,
                             outline="#eb3434", width=5)

    def deselect(self, canvas):
        self._selected = False
        canvas.itemconfigure(self._id, tag="not_selected", outline="")

    def move(self, canvas, dx=0, dy=0, mode="move"):
        if mode == "to":
            self.move_to(canvas, dx, dy)
        elif mode == "move":
            self.update_points(dx, dy, mode)
            canvas.move(self._id, dx, dy)

    def move_to(self, canvas, x, y):
        pass

    def fix_collision(self, canvas, window_size):
        if window_size[0] < canvas.winfo_width():
            win_x = window_size[0]
        else:
            win_x = canvas.winfo_width() - MAGIC_ADD_CONST
        if window_size[1] < canvas.winfo_height():
            win_y = window_size[1]
        else:
            win_y = canvas.winfo_height() - MAGIC_ADD_CONST
        # print(self._x, self._y, win_x, win_y)
        # print(canvas.winfo_width(), canvas.winfo_height())
        if self._x - self._size <= 0:
            print("collision left")
            self.move(canvas, self._size + MAGIC_ADD_CONST, self._y, "to")
        if self._x + self._size >= win_x - MAGIC_ADD_CONST:
            print("collision right")
            self.move(canvas, win_x - self._size - MAGIC_ADD_CONST * 1.5, self._y, "to")
        if self._y - self._size <= 0:
            print("collision up")
            self.move(canvas, self._x, self._size + MAGIC_ADD_CONST, "to")
        if self._y + self._size >= win_y:
            print("collision down")
            self.move(canvas, self._x, win_y - self._size - MAGIC_ADD_CONST / 2, "to")

    def detect_collision(self, canvas, window_size):
        if window_size[0] < canvas.winfo_width():
            win_x = window_size[0]
        else:
            win_x = canvas.winfo_width() - MAGIC_ADD_CONST
        if window_size[1] < canvas.winfo_height():
            win_y = window_size[1]
        else:
            win_y = canvas.winfo_height() - MAGIC_ADD_CONST
        if self._x - self._size <= 0:
            # left
            return "l"
        if self._x + self._size >= win_x:
            # right
            return "r"
        if self._y - self._size <= 0:
            # up
            return "u"
        if self._y + self._size >= win_y:
            # down
            return "d"
        return False

    def delete(self, canvas):
        canvas.delete(self._id)

    def save(self, file_path="new.txt"):
        # return f"['{self}', {self._x}, {self._y}, {self._size}, '{self._color}', {self._selected}]"
        return {"elem": (str(self), self._x, self._y, self._size, self._color, self._selected)}

    def load(self, tuple_attr):
        self._x = tuple_attr[1]
        self._y = tuple_attr[2]
        self._size = tuple_attr[3]
        self._color = tuple_attr[4]
        self._selected = tuple_attr[5]
        self.update_points(self._x, self._y, "to")
