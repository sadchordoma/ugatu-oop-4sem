from abc import ABC, abstractmethod


class FigureFactory(ABC):
    @abstractmethod
    def create_figure(self, name, x, y, size, color, selected):
        pass
