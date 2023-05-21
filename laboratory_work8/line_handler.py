from observer.observer import Observer


class LineHandler(Observer):
    def __init__(self, first, second):
        self.begin = first  # 1 object
        self.end = second  # 2 object
        self.line = -1
        self.triangle = -1

    def move(self, canvas, dx=0, dy=0, mode="move", is_primary=False):
        if self.begin == self.end == "":
            print("was killed")
            return -1
        if is_primary:
            self.end.move(canvas, dx, dy, mode)
        self.delete(canvas)
        self.line = canvas.create_line(self.begin.x, self.begin.y, self.end.x, self.end.y)
        self.triangle = canvas.create_polygon(self.end.x - 10, self.end.y + 10, self.end.x + 10, self.end.y + 10,
                                              self.end.x, self.end.y - 10)

    def delete(self, canvas):
        canvas.delete(self.line)
        canvas.delete(self.triangle)

    def draw(self, canvas):
        self.line = canvas.create_line(self.begin.x, self.begin.y, self.end.x, self.end.y)
        self.triangle = canvas.create_polygon(self.end.x - 10, self.end.y + 10, self.end.x + 10, self.end.y + 10,
                                              self.end.x, self.end.y - 10)

    def remove(self, canvas):
        self.delete(canvas)
        self.begin = ""
        self.end = ""

    def on_object_changed(self, _object):
        pass
