from figures.element import Element


class Group(Element):
    def __init__(self):
        super().__init__()
        self.__shapes = []
        self._id = id(self)

    def __str__(self):
        return "Group"

    def __len__(self):
        return len(self.__shapes)

    @property
    def id(self):
        return self._id

    @property
    def selected(self):
        return self._selected

    def set_color(self, canvas, color):
        for shape in self.__shapes:
            shape.set_color(canvas, color)

    def add_shape(self, shape):
        self.__shapes.append(shape)

    def move(self, canvas, dx, dy, mode="move"):
        for shape in self.__shapes:
            shape.move(canvas, dx, dy, mode)

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

    def update_points(self, dx, dy, mode="move"):
        for shape in self.__shapes:
            shape.update_points(dx, dy, mode)

    def load(self, dict_group):
        pass

    def save(self, file_path="new.txt"):
        # s = "{'" + str(self) + "':"
        # for i in range(len(self.__shapes)):
        #     s += self.__shapes[i].save("new.txt")
        #     if i != len(self.__shapes) - 1:
        #         s += ","
        #
        # return s + "}"
        s = []
        for shape in self.__shapes:
            s.append(shape.save())
        return {"group": s}
