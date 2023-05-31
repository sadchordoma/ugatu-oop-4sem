from observer.observer import Observer
from observer.observable import Observable


class TreeHandler(Observer, Observable):
    def __init__(self, tk_tree):
        super().__init__()
        self._tree = tk_tree

    def on_object_changed(self, _object):
        if len(_object.get_figures()) == 0:
            self.delete_all()
        selected_figures, last_command = _object.get_current_state()
        if last_command[0] == "+":
            self.insert("", "end", last_command[1].id, last_command[1])
        elif last_command[0] == "-":
            self.delete(last_command[1].id)
        self._tree.selection_set([figure.id for figure in selected_figures])
        _object.last_command = 0, 0

    def insert(self, parent, index, iid, _object):
        node = self._tree.insert(parent=parent, index=index, iid=iid,
                                 values=(str(_object), _object.id), text="\t" + str(_object))
        if str(_object) == "Group":
            for figure in _object.group_elems:
                self.delete(figure.id)
                self.insert(node, "end", figure.id, figure)
        return node

    def delete(self, index=-1):
        if index == -1:
            selected_item = self._tree.selection()[0]
            self._tree.delete(selected_item)
            return
        for record in self._tree.get_children():
            values_record = self._tree.item(record)["values"]
            if values_record[1] == index:
                self._tree.delete(record)
                return

    def delete_all(self):
        for record in self._tree.get_children():
            self._tree.delete(record)

    def handle_select(self):
        self.notify_everyone()

    def get_selected(self):
        return [int(i) for i in self._tree.selection()]
