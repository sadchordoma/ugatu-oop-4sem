from tkinter import Canvas
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x: int, y: int, r: int, color: str):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__id = -1
        self.color = color
        self.selected = False

    def get_id(self):
        return self.__id

    def set_color(self, color: str):
        self.color = color

    def select(self, canvas):
        self.selected = True
        canvas.itemconfigure(self.__id, fill=self.color, tag="selected",
                             outline="#eb3434", width=5)