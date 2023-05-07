from tkinter import Canvas
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x: int, y: int, r: int):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__id = -1

    @abstractmethod
    def select(self, canvas: Canvas):
        pass
