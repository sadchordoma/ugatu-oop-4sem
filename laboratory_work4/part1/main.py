from tkinter import Tk, Frame, Checkbutton, Canvas
from tkinter import LEFT, BooleanVar

from circle import Circle


class MainWindow:
    def __init__(self):
        self.all_circles = {}

        self.window = Tk()
        self.window.title("laboratory work 4")
        self.window.geometry("800x800")
        self.window.minsize(400, 400)
        self.window.maxsize(1920, 1080)

        self.frame = Frame(self.window, width=1920, height=50, background="white")
        self.frame.pack(side=LEFT)

        self.checkbox_ctrl_var = BooleanVar()
        self.checkbox_ctrl = Checkbutton(self.frame, text="Ctrl", variable=self.checkbox_ctrl_var, onvalue=1,
                                         offvalue=0, padx=5, pady=5, background="orange")
        self.checkbox_ctrl.pack()

        self.checkbox_intersec_var = BooleanVar()
        self.checkbox_intersec = Checkbutton(self.frame, text="What if Intersection",
                                             variable=self.checkbox_intersec_var, onvalue=1, offvalue=0, padx=5, pady=5,
                                             background="orange")

        self.checkbox_intersec.pack()

        self.canvas = Canvas(self.window, width=1920, height=1080, background="grey")
        self.canvas.pack(side=LEFT)

        self.canvas.bind("<Button-1>", self.click_button1)
        self.canvas.bind("<Control-Button-1>", self.ctrl_click_button1)
        self.window.bind("<Delete>", self.delete_selected_circles)

    def click_button1(self, event, to_diselect=True):
        if to_diselect:
            self.diselect_all()
        circles_in_area = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if circles_in_area:
            closest_elem = circles_in_area[0]
            existed_circle = self.all_circles[closest_elem]
            is_element_here, id_elem = existed_circle.validation(event)
            if is_element_here:
                if self.get_state_checkbox_intersec(event):
                    existed_circle.select_circles_area(event, circles_in_area, self.all_circles, self.canvas)
                else:
                    existed_circle = self.all_circles[id_elem]
                    existed_circle.select(self.canvas)
            else:
                # there is no element
                self.add_circle(event)
        else:
            self.add_circle(event)

    def ctrl_click_button1(self, event):
        if self.get_state_checkbox_ctrl(event) and self.get_state_checkbox_intersec(event):
            self.click_button1(event, to_diselect=False)
        elif self.get_state_checkbox_intersec(event):
            self.click_button1(event)
        elif self.get_state_checkbox_ctrl(event):
            self.click_button1(event, to_diselect=False)
        else:
            self.click_button1(event)

    def add_circle(self, event):
        self.diselect_all()
        new_circle = Circle(event.x, event.y)
        new_circle.draw(self.canvas)
        new_circle.select(self.canvas)

        self.all_circles[new_circle.get_id()] = new_circle

    def diselect_all(self):
        if self.all_circles:
            for circle_id, circle in self.all_circles.items():
                print(circle)
                circle.deselect(self.canvas)

    def delete_selected_circles(self, event):
        selected_circles = self.canvas.find_withtag("selected")
        for circle in selected_circles:
            self.all_circles.pop(circle)
        self.canvas.delete("selected")
        last_selected = self.canvas.find_closest(event.x, event.y)
        if last_selected:
            last_selected = last_selected[0]
            self.all_circles[last_selected].select(self.canvas)

    def start(self):
        self.window.mainloop()

    def get_state_checkbox_ctrl(self, event):
        return self.checkbox_ctrl_var.get()

    def get_state_checkbox_intersec(self, event):
        return self.checkbox_intersec_var.get()


if __name__ == "__main__":
    window = MainWindow()
    window.start()