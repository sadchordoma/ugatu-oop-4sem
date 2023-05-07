from view import View
from circle import Circle


class Window:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self):
        self.figures = {}
        self.view = View()
        # Binding keys
        self.view.canvas.bind("<Button-1>", self.mouse_click)
        self.view.canvas.bind("<Control-Button-1>", self.ctrl_mouse_click)
        self.view.window.bind("<Delete>", self.delete_selected_figures)

    def start(self):
        self.view.window.mainloop()

    # previous mouse_click
    # def mouse_click(self, event):
    #     # with knowledge of what kind element select it and call method on_click
    #     new_circle = Circle(event.x, event.y)
    #     canvas = event.widget
    #     elements_around = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    #     if len(elements_around):
    #         flag = True
    #         validated_elements = set()
    #         for elem_id in elements_around:
    #             figure = self.all_elements.get(elem_id)
    #             if not figure.validate(event):  # if might to select
    #                 flag = False
    #                 break
    #         if flag:
    #             # Проверку добавить на intersection и выбрать элемент - ибо нарисовать новый там нельзя
    #             del new_circle
    #             print(len(validated_elements), validated_elements)
    #     else:
    #         self.deselect_all()
    #         new_circle.draw(canvas)
    #         self.all_elements[new_circle.get_id()] = new_circle

    # def mouse_click(self, event):
    #     self.deselect_all(event)
    #     # with knowledge of what kind of element select it and call method on_click
    #     new_figure = Circle(event.x, event.y)
    #     canvas = event.widget
    #     elements_around = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    #     for id_figure in elements_around:
    #         figure = self.figures.get(id_figure)
    #         # if it can draw
    #         if not figure.validate_select(event):
    #             print("yes")
    #             print(elements_around)
    #             new_figure.draw(canvas)
    #             self.figures[new_figure.get_id()] = new_figure
    #             return
    #     else:
    #         if len(elements_around) > 0:
    #             self.figures.get(elements_around[0]).select(canvas)
    #         else:
    #             new_figure.draw(canvas)
    #             self.figures[new_figure.get_id()] = new_figure

    # without using canvas.find_overlapping

    def mouse_click(self, event, to_diselect=True):
        if to_diselect:
            self.deselect_all(event)
        # TO-DO CHECK HERE FOR INTERSECTION AND CTRL
        # Creating a figure
        new_figure = Circle(event.x, event.y)
        # Deselect all other figures
        # If there is no figures at all -> then easily draw a new one
        if len(self.figures) == 0:
            print("yes, need to draw")
            new_figure.draw(event.widget)
            self.figures[new_figure.get_id()] = new_figure
            return
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
            print("yes, need to draw")
            # Draw
            new_figure.draw(event.widget)
            # Add to dict of all figures with key = id(figure)
            self.figures[new_figure.get_id()] = new_figure
        # Else - there is already a figure on event.x, event.y
        # so just select it
        else:
            print("no, need to select")
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
                        figure_here.select(event.widget)
            # If checkbox Intersection is not pressed - just select 1
            else:
                self.figures[appr_id].select(event.widget)

    def ctrl_mouse_click(self, event):
        # If Checkbox Ctrl is not pressed
        if not self.view.checkbox_ctrl_var.get():
            self.mouse_click(event)
        # If Checkbox Ctrl is pressed
        else:
            self.mouse_click(event, to_diselect=False)

    def deselect_all(self, event):
        for figure in self.figures.values():
            figure.deselect(event.widget)

    def delete_selected_figures(self, event):
        selected_figures = self.view.canvas.find_withtag("selected")
        for _id in selected_figures:
            self.figures.pop(_id)
        self.view.canvas.delete("selected")
        last_selected = self.view.canvas.find_closest(event.x, event.y)
        if last_selected:
            self.figures[last_selected[0]].select(self.view.canvas)


if __name__ == "__main__":
    with Window() as root:
        root.start()
