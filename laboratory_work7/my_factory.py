from figure_factory import FigureFactory

from figures.circle import Circle
from figures.quad import Quad
from figures.triangle import Triangle
from figures.group import Group


class MyFactory(FigureFactory):
    def create_figure(self, name, x=0, y=0, size=0, color='', selected=False):
        if name == "Circle":
            return Circle(x, y, size, color, selected)
        elif name == "Quad":
            return Quad(x, y, size, color, selected)
        elif name == "Triangle":
            return Triangle(x, y, size, color, selected)
        elif name == "Group":
            return Group(selected)
