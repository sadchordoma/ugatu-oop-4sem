from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x: int, y: int, size: int, color: str):
        self._x = x
        self._y = y
        self._size = size
        self._id = -1
        self.color = color
        self.selected = False
        self.magic_size = 87
        self.magic_add_size = 3

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

    def move(self, canvas, dx=0, dy=0, mode="move"):
        self.update_points(dx, dy, mode)
        canvas.move(self._id, dx, dy)

    @abstractmethod
    def check_collision(self, event, window_size):
        pass

    @abstractmethod
    def update_points(self, x, y, mode="move"):
        pass
# Make Figure.move all in one for every other figures
