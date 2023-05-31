from tkinter import Menu, Button, colorchooser, filedialog, messagebox, \
    BooleanVar, IntVar, StringVar

from tkinter.ttk import Treeview

import customtkinter as ctk

import settings

from storage.my_array import MyFiguresArray
from factory.my_factory import MyFactory
from figures.group import Group

from tree_handler import TreeHandler
from line_handler import LineHandler


class View(ctk.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("laboratory work 8")
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
        self.container_frame = ctk.CTkScrollableFrame(self, label_text="Tree View", width=300, height=1080,
                                                      corner_radius=1, border_width=2, border_color="#ffffff",
                                                      fg_color="grey")
        self.container_frame.grid(row=0, column=2, rowspan=4, columnspan=4, sticky="nsew")

        # for 7 lab
        # menu for popup on <Button-3> for it
        self.menu_popup = Menu(tearoff=0)

        # for 8 lab
        self.tree_columns = ["fig", "id"]
        self.tree_view = Treeview(self.container_frame, height=1080, columns=self.tree_columns, show="tree headings")
        self.tree_view.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew", ipadx=5, ipady=5)
        self.tree_view.column("#0", width=300, minwidth=25)
        self.tree_view.column("fig", width=0, stretch=False)
        self.tree_view.column("id", width=0, stretch=False)
        self.tree_view.heading("#0", anchor="center")

    def change_value_scale(self, event):
        self.label_scale_var.set(f"Value for Size : {self.scale_var.get()}")


class App(View):

    def __str__(self):
        return "App"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(self):
        super().__init__()
        # storage, factory, current color/size
        self.figures = MyFiguresArray()
        self.factory = MyFactory()
        self.current_color = "#34eb95"
        self.current_size = settings.SIZE
        # added for 8 lab
        self.tree_handler = TreeHandler(self.tree_view)
        # add observers
        self.tree_handler.add_observer(self.figures)
        self.figures.add_observer(self.tree_handler)
        # Binding keys
        self.file_menu.add_command(label="Load", command=self.load_state_from_file)
        self.file_menu.add_command(label="Save", command=self.save_current_state_figures)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<Control-Button-1>", self.ctrl_mouse_click)
        self.bind("<Delete>", self.delete_selected_figures)

        # To change color on button
        self.color_btn.bind("<Button-1>", self.set_color_from_ask)
        self.curr_color_label.bind("<Button-1>", self.set_color)
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
        self.canvas.bind("<Button-3>", self.context_menu_popup)
        self.canvas.bind("<<Create-Group>>", self.group_shapes)
        self.canvas.bind("<<Remove-Group>>", self.ungroup_shapes)
        # Bind menu_popup to generate event
        self.menu_popup.add_command(label="Group selected figures",
                                    command=lambda: self.canvas.event_generate("<<Create-Group>>"))
        self.menu_popup.add_command(label="Ungroup selected figures",
                                    command=lambda: self.canvas.event_generate("<<Remove-Group>>"))
        # added for 8 lab
        self.tree_view.bind("<ButtonRelease>", self.handle_select_tree)
        self.menu_draw = Menu(self.menu_popup, tearoff=0)
        self.menu_draw.add_command(label="Begin Line", command=lambda: self.handle_draw_line(False))
        self.menu_draw.add_command(label="End Line", command=lambda: self.handle_draw_line(True))
        self.menu_popup.add_cascade(label="Draw line", menu=self.menu_draw)

        self.begin = 0
        self.end = 0
        self.line_handler = LineHandler()

    def handle_draw_line(self, processed):
        if len(self.figures.get_selected_figures()) > 1:
            messagebox.showerror("Error", "Selected > 1 figure to draw line from\n"
                                          "Need to select one object to another")
            return
        if not processed:
            self.begin = self.figures.get_selected_figures()[0]
        else:
            self.end = self.figures.get_selected_figures()[0]
        if self.begin != 0 and self.end != 0:
            if self.begin == self.end:
                messagebox.showerror("Error", "You can not select begin and end of line the same!")
                self.begin = self.end = 0
                return
            # begin start to observe end
            self.begin.figure_observable.add_observer(self.end)
            # end start be observable to start
            self.end.figure_observer.add_parent(self.begin)
            self.begin.figure_observable.draw_lines(self.canvas, self.begin)
            self.end = self.begin = 0

    # Change current size and size of selected figures
    def set_changed_size(self, var=0, index=0, mode=0):
        self.current_size = self.scale_var.get()
        for figure in self.figures.get_selected_figures():
            figure.resize(self.canvas, self.current_size, self.get_window_size())

    def get_window_size(self):
        # 600x600+52+52
        window_size = tuple(map(int, self.winfo_geometry()
                                .replace("+", "x").split("x")[:2]))
        # 600, 600
        return window_size[0], window_size[1]

    # Change color after colorchooser
    def set_color_from_ask(self, event):
        self.current_color = colorchooser.askcolor()[1]
        for figure in self.figures.get_selected_figures():
            figure.set_color(self.canvas, self.current_color)
            figure.select(self.canvas)
        self.curr_color_label.config(background=str(self.current_color))

    # Change color of selected figures
    def set_color(self, event):
        for figure in self.figures.get_selected_figures():
            figure.set_color(self.canvas, self.current_color)

    def start(self):
        self.mainloop()

    def check_collision(self, event):
        for figure in self.figures.get_selected_figures():
            figure.fix_collision(self.canvas, self.get_window_size())

    def key_pressed(self, event=None):
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

        for figure in self.figures.get_selected_figures():
            figure.update_points(dx * 1.5, dy * 1.5, "move")
            if figure.detect_collision(self.canvas, self.get_window_size()):
                figure.update_points(-dx * 1.5, -dy * 1.5, "move")
            else:
                figure.move(self.canvas, dx, dy, "move")

        self.canvas.event_generate("<<Refresh>>")

    def deselect_all(self, event):
        for figure in self.figures:
            figure.deselect(self.canvas)

    def create_figure_from_combobox(self, event):
        selected_combobox_figure = self.combo_figures.get()
        self.focus_set()
        return self.factory.create_figure(selected_combobox_figure,
                                          event.x, event.y, self.current_size, self.current_color,
                                          False)

    def delete_selected_figures(self, event):
        list_to_delete = []
        for figure in self.figures.get_selected_figures():
            figure.delete(self.canvas)
            list_to_delete.append(figure)
        for item in list_to_delete:
            self.figures.remove(item)
        for figure in self.figures:
            if not figure.selected:
                figure.select(self.canvas)
                break
        self.figures.notify_everyone()

    def delete_all(self):
        for figure in self.figures:
            figure.delete(self.canvas)
        self.figures.delete_all()

    # without using canvas.find_overlapping
    def mouse_click(self, event, to_deselect=True):
        # Deselect all other figures
        if to_deselect:
            self.deselect_all(event)
        # If there is no figures at all -> then easily draw a new one
        if len(self.figures) == 0:
            # Creating a figure
            new_figure = self.create_figure_from_combobox(event)
            # print("yes, need to draw")
            new_figure.draw(event.widget)
            new_figure.select(event.widget)
            self.figures.append(new_figure)
        else:
            # Otherwise
            appr_id = -1
            to_draw = True
            # Checking all figures in my dict
            for figure in self.figures:
                # if a cords where I clicked match any figure
                # then select it and break
                # otherwise I can find a figure that is not on my cords will say
                # hmm let's draw there it doesn't match to me
                # but previously there was a figure that said NO
                # that's why [break]
                if figure.validate_select(event):
                    appr_id = figure.id
                    to_draw = False
                    break
                # If I didn't find any figure said current cords match it
                # -> then I can draw
                else:
                    to_draw = True
            # If there is no figure on event.x, event.y
            if to_draw:
                # Draw
                new_figure = self.create_figure_from_combobox(event)
                new_figure.draw(event.widget)
                new_figure.select(event.widget)
                # Add to dict of all figures with key = id(figure)
                self.figures.append(new_figure)
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
                        figure_here = self.figures.find_by_id(_id)
                        # If figure match event.x and event.y
                        # then -> select figure
                        if figure_here.validate_select(event):
                            # Set figure color if it was changed
                            figure_here.select(event.widget)
                # Else if checkbox Intersection is not pressed - just select 1
                else:
                    # Set figure color if it was changed
                    that_figure = self.figures.find_by_id(appr_id)
                    that_figure.select(event.widget)
                self.figures.notify_everyone()
        event.widget.event_generate("<<Refresh>>")

    def ctrl_mouse_click(self, event):
        # If Ctrl is Pressed
        self.mouse_click(event, to_deselect=False)
        self.figures.notify_everyone()

    def refresh(self, event):
        self.set_changed_size()
        self.check_collision(event)

    # added for 7 lab
    def group_shapes(self, event):
        selected_figures = self.figures.get_selected_figures()
        if len(selected_figures) <= 1:
            messagebox.showerror("Error", "Selected only one figure\nNeed at least 2")
            return
        new_group = Group()
        list_to_delete = []
        for figure in selected_figures:
            new_group.add_shape(figure)
            list_to_delete.append(figure)
        self.figures.append(new_group)
        for item in list_to_delete:
            self.figures.remove(item)
            new_group.select(self.canvas)

    def ungroup_shapes(self, event):
        selected_figures = self.figures.get_selected_figures()
        list_to_delete = []
        list_to_add = []
        for figure in selected_figures:
            if str(figure) == "Group":
                list_to_delete.append(figure)
                for shape in figure.group_elems:
                    list_to_add.append(shape)
        for shape in list_to_delete:
            self.figures.remove(shape)
            shape.delete(self.canvas)
        for shape in list_to_add:
            shape.draw(self.canvas)
            self.figures.append(shape)

    def context_menu_popup(self, event):
        self.menu_popup.post(event.x_root, event.y_root)

    def save_current_state_figures(self):
        file_path = filedialog.askopenfilename(title="Save File", initialfile="save.txt", defaultextension=".txt")
        try:
            self.figures.save_figures(file_path)
            messagebox.showinfo("Notification", f"Saved to {file_path}")
        except FileNotFoundError:
            pass

    def load_state_from_file(self):
        file_path = filedialog.askopenfilename(initialfile="save.txt", defaultextension=".txt")
        if file_path != "":
            self.delete_all()
            self.figures.load_figures(file_path, self.factory, self.canvas)
            messagebox.showinfo("Success", f"Loaded from {file_path}")

    # added for 8 lab
    def handle_select_tree(self, event):
        self.deselect_all(self.canvas)
        self.tree_handler.handle_select()
        for figure in self.figures:
            if figure.selected:
                figure.select(self.canvas)
            else:
                figure.deselect(self.canvas)


if __name__ == '__main__':
    with App() as app:
        app.start()
