from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x: int, y: int, size: int, color: str):
        self._x = x
        self._y = y
        self._size = size
        self._id = -1
        self.color = color
        self.selected = False

    def get_id(self):
        return self._id

    def set_color(self, color: str):
        self.color = color

    def select(self, canvas):
        self.selected = True
        canvas.itemconfigure(self._id, fill=self.color, tag="selected",
                             outline="#eb3434", width=5)

    def deselect(self, canvas):
        self.selected = False
        canvas.itemconfigure(self._id, tag="not_selected", outline="")

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
    def move(self, canvas, dx=0, dy=0):
        pass

    @abstractmethod
    def check_collision(self, event, window_size):
        pass
