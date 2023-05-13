from tkinter import Tk, Menu, Frame, Canvas, Checkbutton, Button, \
    BooleanVar, IntVar, StringVar, BOTTOM, VERTICAL, RIGHT, Y

from tkinter.ttk import Scale, Label, Combobox, Scrollbar

import settings


class View:
    def __init__(self):
        # Creating window
        self.window = Tk()
        self.window.title("laboratory work 6")
        self.window.geometry("600x600")
        self.window.minsize(600, 600)
        self.window.maxsize(800, 800)
        self.window.config(bg="#9db3ab")

        # Creating layout for widgets
        self.frame_menu = Frame(self.window, background="#c7d4cf")
        self.frame_menu.grid(row=0, column=0, columnspan=2, sticky="wens")
        # ComboBox for figures
        self.selected_figure = StringVar()
        self.combo_figures = Combobox(self.frame_menu, textvariable=self.selected_figure,
                                      values=settings.available_figures, state="readonly")
        self.combo_figures.grid(row=0, column=5, padx=5, pady=5, sticky="wens")
        # self.combo_figures.pack()
        self.combo_figures.set(settings.available_figures[0])

        # Label for Scale
        self.label_scale_var = StringVar()
        self.label_scale_var.set(f"Value for Size : {settings.SIZE}")
        self.label_scale = Label(self.frame_menu, textvariable=self.label_scale_var, padding=5)
        self.label_scale.grid(row=0, column=0, padx=5, pady=5, sticky="wens")
        # self.label_scale.pack()
        # Scale for changing size of figures
        self.scale_var = IntVar()
        self.scale_var.set(settings.SIZE)
        self.scale = Scale(self.frame_menu, from_=settings.SIZE, to=settings.MAX_SIZE, length=100, value=25,
                           variable=self.scale_var,
                           command=self.change_value_scale)
        self.scale.grid(row=1, column=0, padx=5, pady=5, sticky="wens")
        # self.scale.pack()
        # Checkboxes
        # Checkbox Ctrl
        self.checkbox_ctrl_var = BooleanVar()
        self.checkbox_ctrl = Checkbutton(self.frame_menu, variable=self.checkbox_ctrl_var,
                                         offvalue=0, text="Ctrl",
                                         padx=5, pady=5, background="#9db3ab")
        self.checkbox_ctrl.grid(row=0, column=1, padx=5, pady=5, sticky="wens")
        # self.checkbox_ctrl.pack()
        # Checkbox Intersection
        self.checkbox_intersect_var = BooleanVar()
        self.checkbox_intersect = Checkbutton(self.frame_menu, variable=self.checkbox_intersect_var,
                                              onvalue=1, text="Intersection",
                                              padx=5, pady=5, background="#9db3ab")
        self.checkbox_intersect.grid(row=1, column=1, padx=5, pady=5, sticky="wens")
        # self.checkbox_intersect.pack()
        # Button to select color
        self.button_color = Button(self.frame_menu, text="Pick a Color", background="#9db3ab",
                                   padx=4, pady=4)
        self.button_color.grid(row=0, column=2, padx=5, pady=5, sticky="wens")
        # self.button_color.pack()
        # Creating a menu
        self.panel_menu = Menu()
        self.window.config(menu=self.panel_menu)
        self.panel_menu.add_command(label="1")
        self.panel_menu.add_command(label="2")
        self.panel_menu.add_command(label="3")

        # Creating a frame for canvas for drawing
        self.frame_canvas = Frame(self.window, width=800, height=800, bg="grey")
        self.frame_canvas.grid(row=1, column=0, columnspan=2)

        self.canvas = Canvas(self.frame_canvas, width=800, height=800, bg="#9db3ab")
        self.canvas.pack(side=BOTTOM)

    def change_value_scale(self, event):
        self.label_scale_var.set(f"Value for Size : {self.scale_var.get()}")
