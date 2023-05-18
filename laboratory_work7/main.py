from tkinter import Menu, Button, colorchooser, filedialog, messagebox, BooleanVar, IntVar, StringVar
import customtkinter as ctk

import settings

from my_factory import MyFactory
from figures.group import Group


class App(ctk.CTk):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self):
        super().__init__()

        # configure window
        self.title("laboratory work 7")
        self.minsize(600, 400)
        self.maxsize(1600, 800)
        self.geometry(f"{1600}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # menu
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Load", command=self.load_state_from_file)
        self.file_menu.add_command(label="Save", command=self.save_current_state_figures)

        self.menu.add_separator()
        # self.menu.add_command(label="History of commands")

        # menu for changing these fields: size, intersection, color
        self.menu_frame = ctk.CTkFrame(self, corner_radius=0, height=150)
        self.menu_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.menu_frame.grid_rowconfigure(1, weight=1)
        self.menu_frame.grid_columnconfigure(6, weight=1)
        # ComboBox for figures
        self.selected_figure = StringVar()
        self.combo_figures = ctk.CTkComboBox(self.menu_frame,
                                             values=settings.FIGURES, state="readonly")
        self.combo_figures.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.combo_figures.set(settings.FIGURES[0])

        # Label for Scale
        self.label_scale_var = StringVar()
        self.label_scale_var.set(f"Value for Size : {settings.SIZE}")
        self.label_scale = ctk.CTkLabel(self.menu_frame, textvariable=self.label_scale_var)
        self.label_scale.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Scale for changing size of figures
        self.scale_var = IntVar()
        self.scale_var.set(settings.SIZE)
        self.scale = ctk.CTkSlider(self.menu_frame, from_=settings.SIZE, to=settings.MAX_SIZE,
                                   variable=self.scale_var,
                                   command=self.change_value_scale)
        self.scale.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        # Checkbox Intersection
        self.checkbox_intersect_var = BooleanVar()
        self.checkbox_intersect = ctk.CTkCheckBox(self.menu_frame, variable=self.checkbox_intersect_var,
                                                  onvalue=1, text="Intersection")
        self.checkbox_intersect.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        # Current Color Button
        self.curr_color_label = Button(self.menu_frame, text="Current Color", background="#34eb95")
        self.curr_color_label.grid(row=0, column=4, padx=5, pady=5, sticky="nsew")

        # Button to select color
        self.color_btn = ctk.CTkButton(self.menu_frame, text="Pick a Color")
        self.color_btn.grid(row=0, column=5, padx=5, pady=5, sticky="nsew")

        # create sidebar frame with widgets
        # canvas frame
        self.canvas_frame = ctk.CTkFrame(self, width=800, corner_radius=0)
        self.canvas_frame.grid(row=1, column=0, rowspan=4, columnspan=2, sticky="nsew")
        self.canvas_frame.grid_rowconfigure(2, weight=1)

        self.canvas = ctk.CTkCanvas(self.canvas_frame, width=1300, height=980, background="#4d4f4d")
        self.canvas.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew")

        # container frame
        self.container_frame = ctk.CTkScrollableFrame(self, label_text="Container", width=300, height=1080,
                                                      corner_radius=1, border_width=2, border_color="#ffffff")
        self.container_frame.grid(row=0, column=2, rowspan=4, columnspan=4, sticky="nsew")

        #
        self.figures = {}
        self.current_color = "#34eb95"
        self.current_size = settings.SIZE

        # Binding keys
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<Control-Button-1>", self.ctrl_mouse_click)
        self.bind("<Delete>", self.delete_selected_figures)

        # To change color on button
        self.color_btn.bind("<Button-1>", self.set_color)
        # To trace change variable of scale of figures
        self.label_scale_var.trace_add(["write"], self.set_changed_size)
        # To control movement
        self.bind("<KeyPress-Left>", self.key_pressed)
        self.bind("<KeyPress-Right>", self.key_pressed)
        self.bind("<KeyPress-Up>", self.key_pressed)
        self.bind("<KeyPress-Down>", self.key_pressed)

        # bind my own generated events
        self.canvas.bind("<<Refresh>>", self.refresh)
        self.bind("<<Refresh>>", self.refresh)

        # for 7 lab
        # menu for popup and bind <Button-3> for it
        self.menu_popup = Menu(tearoff=0)
        self.menu_popup.add_command(label="Group selected figures",
                                    command=lambda: self.canvas.event_generate("<<Create-Group>>"))
        self.canvas.bind("<Button-3>", self.context_menu_popup)
        self.canvas.bind("<<Create-Group>>", self.group_shapes)

        self.text_box = ctk.CTkTextbox(self.container_frame, width=300, height=1080, state="disabled")
        self.text_box.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew")

        self.factory = MyFactory()

    def change_value_scale(self, event):
        self.label_scale_var.set(f"Value for Size : {self.scale_var.get()}")

    def set_changed_size(self, var=0, index=0, mode=0):
        # Change current size and size of selected figures
        self.current_size = self.scale_var.get()
        for _id, figure in self.figures.items():
            if figure.selected:
                figure.resize(self.canvas, self.current_size, self.get_window_size())

    def get_window_size(self):
        # 600x600+52+52
        window_size = tuple(map(int, self.winfo_geometry()
                                .replace("+", "x").split("x")[:2]))
        return window_size[0], window_size[1]

    # Set color for drawing figures
    def set_color(self, event):
        self.current_color = colorchooser.askcolor()[1]
        for _id in self.get_id_selected_figures():
            if self.figures[_id].selected:
                self.figures[_id].set_color(self.canvas, self.current_color)
                self.figures[_id].select(self.canvas)
        self.curr_color_label.config(background=str(self.current_color))

    def start(self):
        self.mainloop()

    def check_collision(self, event):
        for _id, figure in self.figures.items():
            if figure.selected:
                figure.fix_collision(self.canvas, self.get_window_size())

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

        for _id, figure in self.figures.items():
            if figure.selected:
                figure.update_points(dx * 1.5, dy * 1.5, "move")
                if figure.detect_collision(self.canvas, self.get_window_size()):
                    figure.update_points(-dx * 1.5, -dy * 1.5, "move")
                else:
                    figure.move(self.canvas, dx, dy, "move")

        event.widget.event_generate("<<Refresh>>")

    def deselect_all(self, event):
        for figure in self.figures.values():
            figure.deselect(event.widget)

    def create_figure_from_combobox(self, event):
        selected_combobox_figure = self.combo_figures.get()
        self.focus_set()
        return self.factory.create_figure(selected_combobox_figure,
                                          event.x, event.y, self.current_size, self.current_color,
                                          False)

    def delete_selected_figures(self, event):
        selected_figures = self.get_id_selected_figures()

        for _id in selected_figures:
            self.figures[_id].delete(self.canvas)
            self.figures.pop(_id)
        for _id in self.figures:
            if not self.figures[_id].selected:
                self.figures[_id].select(self.canvas)
                break

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
            new_figure.select(event.widget)
            self.figures[new_figure.id] = new_figure
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
                new_figure.select(event.widget)
                # Add to dict of all figures with key = id(figure)
                self.figures[new_figure.id] = new_figure
            # Else - there is already a figure on event.x, event.y
            # so just select it
            else:
                chkbox_intersec = self.checkbox_intersect_var.get()
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
                            figure_here.set_color(event.widget, self.current_color)
                            figure_here.select(event.widget)
                # Else if checkbox Intersection is not pressed - just select 1
                else:
                    # Set figure color if it was changed
                    self.figures[appr_id].set_color(event.widget, self.current_color)
                    self.figures[appr_id].select(event.widget)
        event.widget.event_generate("<<Refresh>>")

    def ctrl_mouse_click(self, event):
        # If Ctrl is Pressed
        self.mouse_click(event, to_deselect=False)

    def refresh(self, event):
        self.set_changed_size()
        self.check_collision(event)

    # added for 7 lab
    def group_shapes(self, event, id_selected=None):
        if id_selected is None:
            id_selected = self.get_id_selected_figures()
        new_group = Group()
        for _id in id_selected:
            new_group.add_shape(self.figures[_id])
            self.figures.pop(_id)
            self.figures[id(new_group)] = new_group

    def context_menu_popup(self, event):
        self.menu_popup.post(event.x_root, event.y_root)

    def get_id_selected_figures(self):
        id_selected_figures = []
        for _id, figure in self.figures.items():
            if figure.selected:
                id_selected_figures.append(_id)
        return id_selected_figures

    def save_current_state_figures(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        try:
            with open(file_path, "w") as f:
                #     for item in self.canvas.find_all():
                #         print(json.dumps({
                #             'type': self.canvas.type(item),
                #             'coords': self.canvas.coords(item),
                #             'options': {key: val[-1] for key, val
                #                         in self.canvas.itemconfig(item).items()}
                #         }), file=f)
                f.write("name x y size color selected\n")
                for figure in self.figures.values():
                    f.write(str(figure.save("new.txt")) + "\n")
            messagebox.showinfo("Notification", f"Saved to {file_path}")
        except FileNotFoundError:
            pass

    def load_elem(self, attr_figures):
        new_figure = self.factory.create_figure(attr_figures[0])
        new_figure.load(attr_figures)
        new_figure.draw(self.canvas)
        self.figures[new_figure.id] = new_figure
        return new_figure

    def load_group(self, group, rec=None):
        ids_group = []
        for i in range(len(group)):
            if group[i].get("elem"):
                new_figure = self.load_elem(group[i]["elem"])
                ids_group.append(new_figure.id)
            elif group[i].get("group"):
                list_group = group[i]["group"]
                ids = self.load_group(list_group, "rec")
                for _id in ids:
                    ids_group.append(_id)
                self.group_shapes(event=None, id_selected=ids_group)

        if len(ids_group) > 0 and rec is None:
            self.group_shapes(event=None, id_selected=ids_group)
        return ids_group

    def load_state_from_file(self):
        # open file
        # create fabric
        # create shape array
        # call load shapes
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        f = open(file_path, "r")
        s = f.readlines()
        if s[0] != "name x y size color selected\n":
            messagebox.showerror("Error", "Corrupted File")
            raise Exception("Corrupted File")
        for line in s[1:]:
            dict_figure = eval(line)
            print(dict_figure)
            if dict_figure.get("elem"):
                self.load_elem(dict_figure["elem"])
            elif dict_figure.get("group"):
                self.load_group(dict_figure["group"])
        f.close()

    # def load_shapes(self, file_path: str, figure_factory):
    #     try:
    #         f = open(file_path, "r")
    #         s = f.readlines()
    #         for line in s:
    #             shape = eval(line)
    #             # shape = figure_factory.create_shape(name)
    #             # shape.load(shape)
    #             # self.__shapes.append(shape)
    #             print(type(shape), shape)
    #         f.close()
    #     except FileNotFoundError as e:
    #         raise e


if __name__ == '__main__':
    with App() as app:
        app.start()
