from observer.observable import Observable
from observer.observer import Observer


class MyFiguresArray(Observer, Observable):
    def __init__(self, *args):
        super().__init__()
        self._figures = [*args]
        self._last_command = 0, 0

    def __getitem__(self, index: int):
        return self._figures[index]

    def __str__(self):
        return f"{self._figures}"

    def __len__(self):
        return len(self._figures)

    @property
    def last_command(self):
        return self._last_command

    @last_command.setter
    def last_command(self, last_command):
        self._last_command = last_command

    def append(self, item: object):
        self._figures.append(item)
        self._last_command = "+", item
        self.notify_everyone()

    def at(self, index: int):
        return self._figures[index]

    def remove(self, item: object):
        self._figures.remove(item)
        self._last_command = "-", item
        self.notify_everyone()

    def get_selected_figures(self):
        selected_figures = []
        for figure in self._figures:
            if figure.selected:
                selected_figures.append(figure)
        return selected_figures

    def find_by_id(self, _id: int):
        for figure in self._figures:
            if figure.id == _id:
                return figure
        print(f"No such figure with id={_id}")
        return None

    def load_figures(self, file_path: str, figure_factory, canvas=None):
        f = open(file_path, "r")
        first_line = f.readline()
        if first_line != "SOME WORDS TO CHECK IF FILE WASNT CORRUPTED\n":
            raise Exception("Corrupted File")
        f.readline()
        self.delete_all()
        while True:
            s = f.readline().strip()
            print("f.readline()", s)
            if not s:
                f.close()
                break
            if s == "Group":
                figure = figure_factory.create_figure("Group")
                print("Group", figure)
                len_group = int(f.readline())
                print("len_group", len_group)
                figure.load(f, figure_factory, _len=len_group)
            else:
                figure = figure_factory.create_figure(s)
                print("Figure", figure)
                figure.load(f)
            figure.draw(canvas)
            self.append(figure)

    def save_figures(self, file_path: str):
        with open(file_path, "w") as f:
            f.write("SOME WORDS TO CHECK IF FILE WASNT CORRUPTED\n")
            for figure in self._figures:
                f.write("\n" + str(figure.save()))

    # added for 8 lab
    def on_object_changed(self, _object):
        id_selected = _object.get_selected()
        for figure in self._figures:
            figure.selected = False
        for figure in self._figures:
            for _id in id_selected:
                print(figure.id, _id)
                if figure.id == _id:
                    figure.selected = True

    def get_current_state(self):
        if self.last_command == -1 and len(self._figures) > 0:
            self.last_command = "+", self._figures[0]
        return self.get_selected_figures(), self.last_command

    def get_all_figures(self):
        return self._figures

    def delete_all(self):
        while len(self._figures) > 0:
            for figure in self._figures:
                self.remove(figure)
        self.notify_everyone()
