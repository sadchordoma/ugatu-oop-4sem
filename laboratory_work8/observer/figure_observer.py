# наблюдатель
class FigureObserver:
    def __init__(self):
        self._parents = []

    def on_object_changed(self, canvas):
        for parent in self._parents:
            parent.figure_observable.draw_lines(canvas, parent)

    def add_parent(self, _object):
        self._parents.append(_object)

    def remove_parent(self, _object):
        self._parents.remove(_object)

    def remove_all(self, canvas, _object):
        for parent in self._parents:
            parent.figure_observable.remove_observer(parent, canvas, _object)
        # self.on_object_changed(canvas)
