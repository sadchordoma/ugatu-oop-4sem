from figures.element import Element
from observer.figure_observable import FigureObservable
from observer.figure_observer import FigureObserver


class Group(Element):
    def __init__(self, selected=False):
        super().__init__()
        self.__shapes = []
        self._selected = selected
        self._id = id(self)
        self.figure_observer = FigureObserver()
        self.figure_observable = FigureObservable()
        self.checked = False

    @property
    def x(self):
        for shape in self.__shapes:
            return shape.x

    @property
    def y(self):
        for shape in self.__shapes:
            return shape.y

    @property
    def group_elems(self):
        return self.__shapes

    def __getitem__(self, index: int):
        return self.__shapes[index]

    def __str__(self):
        return "Group"

    def view(self):
        return f"{self.__shapes}"

    def __len__(self):
        return len(self.__shapes)

    def first(self):
        return self.__shapes[0]

    @property
    def id(self):
        return self._id

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value

    def set_color(self, canvas, color):
        for shape in self.__shapes:
            shape.set_color(canvas, color)

    def add_shape(self, shape):
        self.__shapes.append(shape)

    def move(self, canvas, dx, dy, mode="move"):
        for shape in self.__shapes:
            shape.move(canvas, dx, dy, mode)
        self.figure_observable.notify_everyone(canvas, dx, dy)
        self.figure_observer.on_object_changed(canvas)

    def draw(self, canvas):
        for shape in self.__shapes:
            shape.draw(canvas)

    def select(self, canvas):
        self._selected = True
        for shape in self.__shapes:
            shape.select(canvas)

    def deselect(self, canvas):
        self._selected = False
        for shape in self.__shapes:
            shape.deselect(canvas)

    def fix_collision(self, canvas, window_size):
        for shape in self.__shapes:
            shape.fix_collision(canvas, window_size)

    def detect_collision(self, canvas, window_size):
        for shape in self.__shapes:
            flag = shape.detect_collision(canvas, window_size)
            if flag:
                return True
        return False

    def resize(self, canvas, size, window_size):
        for shape in self.__shapes:
            shape.resize(canvas, size, window_size)

    def validate_select(self, event):
        for shape in self.__shapes:
            flag = shape.validate_select(event)
            if flag:
                return True
        return False

    def delete(self, canvas):
        for shape in self.__shapes:
            shape.delete(canvas)
        self.figure_observable.remove_all(canvas)
        self.figure_observer.remove_all(canvas, self)

    def update_points(self, dx, dy, mode="move"):
        for shape in self.__shapes:
            shape.update_points(dx, dy, mode)

    def load(self, file, figure_factory):
        group_len = int(file.readline())
        for i in range(group_len):
            s = file.readline().strip()
            print(s)
            figure = figure_factory.create_figure(s)
            figure.load(file, figure_factory)
            self.__shapes.append(figure)

    def save(self):
        shapes = []
        for shape in self.__shapes:
            shapes.append(shape.save())
        s = f"Group\n{len(shapes)}"
        for shape in shapes:
            s += "\n" + str(shape)
        return s

    def find_by_id(self, _id: int):
        for shape in self.__shapes:
            shape.find(_id)
