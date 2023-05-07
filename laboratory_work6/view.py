from tkinter import Tk, Menu, Frame, Canvas, Checkbutton
from tkinter.ttk import Separator
from tkinter import HORIZONTAL, BooleanVar


class View:
    def __init__(self):
        # Creating window
        self.window = Tk()
        self.window.title("laboratory work 6")
        self.window.geometry("800x800")
        self.window.minsize(400, 400)
        self.window.maxsize(1920, 1080)
        self.window.config(bg="#9db3ab")

        # Creating layout for widgets
        self.frame_menu = Frame(self.window, width=1920, height=50, background="#c7d4cf")
        self.frame_menu.grid(row=0, column=0)
        # Checkboxes

        # Checkbox Ctrl
        self.checkbox_ctrl_var = BooleanVar()
        self.checkbox_ctrl = Checkbutton(self.frame_menu, variable=self.checkbox_ctrl_var,
                                         offvalue=0, text="Ctrl",
                                         padx=5, pady=5, background="#9db3ab")
        self.checkbox_ctrl.grid(row=0, column=0)

        # Checkbox Intersection
        self.checkbox_intersect_var = BooleanVar()
        self.checkbox_intersect = Checkbutton(self.frame_menu, variable=self.checkbox_intersect_var,
                                              onvalue=1, text="Intersection",
                                              padx=5, pady=5, background="#9db3ab")
        self.checkbox_intersect.grid(row=0, column=1)

        # Creating a menu
        self.panel_menu = Menu(self.frame_menu)
        self.window.config(menu=self.panel_menu)
        self.panel_menu.add_command(label="1")
        self.panel_menu.add_command(label="2")
        self.panel_menu.add_command(label="3")

        # Creating separator between 2 frames
        self.horizontal_separator = Separator(master=self.window,
                                              orient=HORIZONTAL,
                                              style="TSeparator",
                                              class_="Separator",
                                              takefocus=1,
                                              cursor="man")
        self.horizontal_separator.grid(row=1, columnspan=2)

        # Creating a frame for canvas for drawing
        self.frame_canvas = Frame(self.window, width=1920, height=1080, bg="grey")
        self.frame_canvas.grid(row=2, column=0, columnspan=2)

        self.canvas = Canvas(self.frame_canvas, width=1920, height=1080, bg="#9db3ab")
        self.canvas.grid(rowspan=2, columnspan=2)
