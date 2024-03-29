from abc import ABC, abstractmethod
from settings import MAGIC_ADD_CONST

from observer.figure_observable import FigureObservable
from observer.figure_observer import FigureObserver


class Figure(ABC):
    def __init__(self, x: int, y: int, size: int, color: str, selected=False):
        self._x = x
        self._y = y
        self._size = size
        self._id = -1
        self._color = color
        self._selected = selected

        self.figure_observable = FigureObservable()
        self.figure_observer = FigureObserver()
        self.checked = False

    def __len__(self):
        return 1

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @abstractmethod
    def __str__(self):
        pass

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

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
        canvas.itemconfigure(self._id, fill=self._color)

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
        canvas.itemconfigure(self._id, tag="selected", outline="#eb3434", width=5)

    def deselect(self, canvas):
        self._selected = False
        canvas.itemconfigure(self._id, tag="not_selected", outline="")

    def move(self, canvas, dx=0, dy=0, mode="move"):
        if mode == "to":
            self.move_to(canvas, dx, dy)
        elif mode == "move":
            self.update_points(dx, dy, mode)
            canvas.move(self._id, dx, dy)
        self.figure_observable.notify_everyone(canvas, dx, dy)
        self.figure_observer.on_object_changed(canvas)
        # self.figure_observable.draw_lines(canvas, self)

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
        self.figure_observable.remove_all(canvas)
        self.figure_observer.remove_all(canvas, self)

    def save(self):
        return f"{str(self)}\n{self._x}, {self._y}, {self._size}, {self._color}, {self._selected}"

    def load(self, file, figure_factory=None):
        s = file.readline()
        print("atr for figure", s)
        tuple_attr = s.split(",")
        self._x = float(tuple_attr[0])
        self._y = float(tuple_attr[1])
        self._size = float(tuple_attr[2])
        self._color = tuple_attr[3].strip()
        self._selected = eval(tuple_attr[4])
        self.update_points(self._x, self._y, "to")
