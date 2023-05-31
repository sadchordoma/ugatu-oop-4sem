# Наблюдаемый
class FigureObservable:
    def __init__(self):
        self._observers = []
        self._lines = []

    @property
    def observers(self):
        return self._observers

    @property
    def lines(self):
        return self._lines

    def add_observer(self, _object):
        self._observers.append(_object)

    def remove_observer(self, figure, canvas, _object):
        if _object in self._observers:
            self._observers.remove(_object)
        self.draw_lines(canvas, figure)

    def remove_all(self, canvas):
        self._observers.clear()
        self.delete_lines(canvas)

    def notify_everyone(self, canvas, dx, dy):
        for observer in self._observers:
            if not observer.checked:
                observer.checked = True
                observer.move(canvas, dx, dy)
        self.make_all_not_checked()

    def draw_lines(self, canvas, figure):
        self.delete_lines(canvas)
        for observer in self._observers:
            self._lines.append(canvas.create_line(figure.x, figure.y, observer.x, observer.y, arrow="last"))

    def delete_lines(self, canvas):
        for line in self._lines:
            canvas.delete(line)

    def make_all_not_checked(self):
        for observer in self._observers:
            observer.checked = False
