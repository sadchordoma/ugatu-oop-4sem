from view import View
from model import Model


class Window:
    # __enter__ / __exit__ - magic methods for use in with .. as ..
    def __enter__(self):
        self.model.open_data()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.model

    def __init__(self):
        self.view = View()

        self.model = Model()
        self.model.observers.append(self.view.window)

        self.view.window.bind("<<UpdateForm>>", self.update_form)
        # Binding Entries
        self.view.entry_a.bind("<FocusOut>",
                               lambda value: self.model.set_value_a(self.view.entry_a.get()))
        self.view.entry_b.bind("<FocusOut>",
                               lambda value: self.model.set_value_b(self.view.entry_b.get()))
        self.view.entry_c.bind("<FocusOut>",
                               lambda value: self.model.set_value_c(self.view.entry_c.get()))

        # Binding SpinBoxes
        self.view.spinbox_a["command"] = \
            lambda: self.model.set_value_a(self.view.spinbox_var_a.get())
        self.view.spinbox_a.bind("<FocusOut>",
                                 lambda value: self.model.set_value_a(self.view.spinbox_var_a.get()))

        self.view.spinbox_b["command"] = \
            lambda: self.model.set_value_b(int(self.view.spinbox_var_b.get()))
        self.view.spinbox_b.bind("<FocusOut>",
                                 lambda value: self.model.set_value_b(self.view.spinbox_var_b.get()))

        self.view.spinbox_c["command"] = \
            lambda: self.model.set_value_c(int(self.view.spinbox_var_c.get()))
        self.view.spinbox_c.bind("<FocusOut>",
                                 lambda value: self.model.set_value_c(self.view.spinbox_var_c.get()))

        # Binding Scales
        self.view.scale_var_a.trace_add("write",
                                        lambda var="a", index=0, mode=0: self.event_from_scale(var="a", index=0,
                                                                                               mode=0))
        self.view.scale_var_b.trace_add("write",
                                        lambda var="b", index=0, mode=0: self.event_from_scale(var="b", index=0,
                                                                                               mode=0))
        self.view.scale_var_c.trace_add("write",
                                        lambda var="c", index=0, mode=0: self.event_from_scale(var="c", index=0,
                                                                                               mode=0))

    def event_from_scale(self, var, index, mode):
        if var == "a":
            self.model.set_value_a(self.view.scale_var_a.get())
        elif var == "b":
            self.model.set_value_b(self.view.scale_var_b.get())
        elif var == "c":
            self.model.set_value_c(self.view.scale_var_c.get())

    def update_form(self, event):
        args = self.model.get_values_all()
        self.view.entry_a.delete(0, "end")
        self.view.entry_a.insert(0, str(args[0]))
        self.view.spinbox_a.set(args[0])
        self.view.scale_a.set(args[0])

        self.view.entry_b.delete(0, "end")
        self.view.entry_b.insert(0, str(args[1]))
        self.view.spinbox_b.set(args[1])
        self.view.scale_b.set(args[1])

        self.view.entry_c.delete(0, "end")
        self.view.entry_c.insert(0, str(args[2]))
        self.view.spinbox_c.set(args[2])
        self.view.scale_c.set(args[2])

    def start(self):
        self.view.window.mainloop()


if __name__ == '__main__':
    with Window() as root:
        root.start()
