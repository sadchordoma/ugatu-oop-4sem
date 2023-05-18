from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self):
        self._selected = False

    @abstractmethod
    def move(self, canvas, dx, dy):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass

    @abstractmethod
    def save(self, path_file):
        pass

    @abstractmethod
    def load(self, attr):
        pass
