from view import View
from circle import Circle
from quad import Quad
from triangle import Triangle

from tkinter import colorchooser


class Window:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self):
        self.view = View()
        self.figures = {}

        self.current_color = "#34eb95"
        self.current_size = 25
        # Binding keys
        self.view.canvas.bind("<Button-1>", self.mouse_click)
        self.view.canvas.bind("<Control-Button-1>", self.ctrl_mouse_click)
        self.view.window.bind("<Delete>", self.delete_selected_figures)

        # To change color on button
        self.view.button_color.bind("<Button-1>", self.set_color)
        # To trace change variable of scale of figures
        self.view.label_scale_var.trace_add(["write"], self.set_changed_size)
        # To control movement
        self.view.window.bind("<KeyPress-Left>", self.key_pressed)
        self.view.window.bind("<KeyPress-Right>", self.key_pressed)
        self.view.window.bind("<KeyPress-Up>", self.key_pressed)
        self.view.window.bind("<KeyPress-Down>", self.key_pressed)

        # bind my own generated events
        self.view.canvas.bind("<<Refresh>>", self.refresh)
        self.view.window.bind("<<Refresh>>", self.refresh)

    def start(self):
        self.view.window.mainloop()

    def check_collision(self, event):
        for _id, figure in self.figures.items():
            if figure.selected:
                figure.check_collision(self.view.canvas, self.get_window_size())

    def get_window_size(self):
        # 600x600+52+52
        window_size = tuple(map(int, self.view.window.winfo_geometry()
                                .replace("+", "x").split("x")[:2]))

        return {"x": window_size[0], "y": window_size[1]}

    # Set color for drawing figures
    def set_color(self, event):
        self.current_color = colorchooser.askcolor()[1]
        self.view.canvas.itemconfigure("selected", fill=self.current_color)
        self.view.current_color.config(background=self.current_color)

    def key_pressed(self, event):
        dist = 5
        dx = 0
        dy = 0
        which_key = {37: "left", 38: "up", 39: "right", 40: "down"}
        if which_key[event.keycode] == "left":
            dx = -dist
        elif which_key[event.keycode] == "right":
            dx = dist
        elif which_key[event.keycode] == "up":
            dy = -dist
        elif which_key[event.keycode] == "down":
            dy = dist

        for _id in self.view.canvas.find_withtag("selected"):
            figure = self.figures[_id]
            figure.move(self.view.canvas, dx, dy, "move")
        event.widget.event_generate("<<Refresh>>")

    def deselect_all(self, event):
        for figure in self.figures.values():
            figure.deselect(event.widget)

    def set_changed_size(self, var=0, index=0, mode=0):
        # Change current size and size of selected figures
        self.current_size = self.view.scale_var.get()
        for _id, figure in self.figures.items():
            if figure.selected:
                figure.resize(self.view.canvas, self.current_size, self.get_window_size())

    def create_figure_from_combobox(self, event):
        selected_combobox_figure = self.view.combo_figures.get()
        self.view.window.focus_set()
        if selected_combobox_figure == "Circle":
            return Circle(event.x, event.y, self.current_size, self.current_color)
        elif selected_combobox_figure == "Quad":
            return Quad(event.x, event.y, self.current_size, self.current_color)
        elif selected_combobox_figure == "Triangle":
            return Triangle(event.x, event.y, self.current_size, self.current_color)

    def delete_selected_figures(self, event):
        selected_figures = self.view.canvas.find_withtag("selected")
        for _id in selected_figures:
            self.figures.pop(_id)
        self.view.canvas.delete("selected")
        last_selected = self.view.canvas.find_closest(event.x, event.y)
        if last_selected:
            self.figures[last_selected[0]].select(self.view.canvas)

    # without using canvas.find_overlapping
    def mouse_click(self, event, to_deselect=True):
        # Deselect all other figures
        if to_deselect:
            self.deselect_all(event)
        # Creating a figure
        new_figure = self.create_figure_from_combobox(event)
        # If there is no figures at all -> then easily draw a new one
        if len(self.figures) == 0:
            # print("yes, need to draw")
            new_figure.draw(event.widget)
            self.figures[new_figure.get_id()] = new_figure
        else:
            # Otherwise
            appr_id = -1
            to_draw = True
            # Checking all figures in my dict
            for _id, figure in self.figures.items():
                # if a cords where I clicked match any figure
                # then select it and break
                # otherwise I can find a figure that is not on my cords will say
                # hmm let's draw there it doesn't match to me
                # but previously there was a figure that said NO
                # that's why [break]
                if figure.validate_select(event):
                    appr_id = _id
                    to_draw = False
                    break
                # If I didn't find any figure said current cords match it
                # -> then I can draw
                else:
                    to_draw = True
            # If there is no figure on event.x, event.y
            if to_draw:
                # Draw
                new_figure.draw(event.widget)
                # detect whether there is a collision
                # Add to dict of all figures with key = id(figure)
                self.figures[new_figure.get_id()] = new_figure
            # Else - there is already a figure on event.x, event.y
            # so just select it
            else:
                chkbox_intersec = self.view.checkbox_intersect_var.get()
                # If checkbox Intersection is pressed
                if chkbox_intersec:
                    # Find all ids of figures in current event.x, event.y
                    ids_intersected_figures = event.widget.find_overlapping(event.x, event.y, event.x, event.y)
                    for _id in ids_intersected_figures:
                        # Get figure from id
                        figure_here = self.figures[_id]
                        # If figure match event.x and event.y
                        # then -> select figure
                        if figure_here.validate_select(event):
                            # Set figure color if it was changed
                            figure_here.set_color(self.current_color)
                            figure_here.select(event.widget)
                # Else if checkbox Intersection is not pressed - just select 1
                else:
                    # Set figure color if it was changed
                    self.figures[appr_id].set_color(self.current_color)
                    self.figures[appr_id].select(event.widget)
        event.widget.event_generate("<<Refresh>>")

    def ctrl_mouse_click(self, event):
        # If Ctrl is Pressed
        self.mouse_click(event, to_deselect=False)

    def refresh(self, event):
        self.set_changed_size()
        self.check_collision(event)


if __name__ == "__main__":
    with Window() as root:
        root.start()
