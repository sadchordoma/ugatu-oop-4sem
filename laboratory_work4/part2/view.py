from tkinter import Tk, Label, Frame, StringVar, IntVar
from tkinter.ttk import Spinbox, Entry, Scale


class View:
    def __init__(self):
        # MainWindow
        self.window = Tk()
        self.window.title("laboratory work 4")
        self.window.geometry("900x400")
        self.window.minsize(400, 400)
        self.window.maxsize(1920, 1080)
        # Creating layout of widgets
        # Frame a
        self.frame_a = Frame(self.window, height=700, width=233, background="grey")
        self.frame_a.grid(row=0, column=0)

        self.label_a = Label(self.frame_a, text="A", font=("Sans Serif", 25),
                             background="grey", padx=5, pady=5, width=10)
        self.label_a.grid(row=1, column=0, sticky="ew")

        self.entry_a = Entry(self.frame_a, width=30)
        self.entry_a.grid(row=2, column=0, sticky="nsew")

        self.spinbox_var_a = StringVar()
        self.spinbox_a = Spinbox(self.frame_a, from_=0, to=100, textvariable=self.spinbox_var_a, width=28)
        self.spinbox_a.grid(row=3, column=0, sticky="nsew")

        self.scale_var_a = IntVar()
        self.scale_a = Scale(self.frame_a, from_=0, to=100, variable=self.scale_var_a, length=200)
        self.scale_a.grid(row=4, column=0, sticky="nsew")

        # Separator of frames a and b
        self.frame_sep_a_b = Frame(self.window, height=700, width=100, background="grey")
        self.frame_sep_a_b.grid(row=0, column=1)
        self.label_sep_a_b = Label(self.frame_sep_a_b, text="<=", font=("Sans Serif", 25), background="grey")
        self.label_sep_a_b.grid()

        # Frame b
        self.frame_b = Frame(self.window, height=700, width=233, background="grey")
        self.frame_b.grid(row=0, column=2, sticky="nsew")

        self.label_b = Label(self.frame_b, text="B", font=("Sans Serif", 25), background="grey", padx=5, pady=5,
                             width=10)
        self.label_b.grid(row=0, column=0, sticky="ew")

        self.entry_b = Entry(self.frame_b, width=30)
        self.entry_b.grid(row=1, column=0, sticky="ew")

        self.spinbox_var_b = StringVar()
        self.spinbox_b = Spinbox(self.frame_b, from_=0, to=100, textvariable=self.spinbox_var_b, width=28)
        self.spinbox_b.grid(row=2, column=0, sticky="ew")

        self.scale_var_b = IntVar()
        self.scale_b = Scale(self.frame_b, from_=0, to=100, variable=self.scale_var_b, length=200)
        self.scale_b.grid(row=3, column=0, sticky="ew")

        # Separator of frames b and c
        self.frame_sep_b_c = Frame(self.window, height=700, width=100, background="grey")
        self.frame_sep_b_c.grid(row=0, column=3)

        self.label_sep_b_c = Label(self.frame_sep_b_c, text="<=", font=("Sans Serif", 25), background="grey")
        self.label_sep_b_c.grid(sticky="nsew")

        # Frame c
        self.frame_c = Frame(self.window, height=700, width=233, background="grey")
        self.frame_c.grid(row=0, column=4, sticky="nsew")

        self.label_c = Label(self.frame_c, text="C", font=("Sans Serif", 25), background="grey", padx=5, pady=5,
                             width=10)
        self.label_c.grid(row=0, column=0, sticky="ew")

        self.entry_c = Entry(self.frame_c, width=30)
        self.entry_c.grid(row=1, column=0, sticky="ew")

        self.spinbox_var_c = StringVar()
        self.spinbox_c = Spinbox(self.frame_c, from_=0, to=100, textvariable=self.spinbox_var_c, width=28)
        self.spinbox_c.grid(row=2, column=0, sticky="ew")

        self.scale_var_c = IntVar()
        self.scale_c = Scale(self.frame_c, from_=0, to=100, variable=self.scale_var_c, length=200)
        self.scale_c.grid(row=3, column=0, sticky="ew")
