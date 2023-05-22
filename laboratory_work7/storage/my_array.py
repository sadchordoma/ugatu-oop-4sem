class MyFiguresArray:
    def __init__(self, *args):
        self._figures = [*args]

    def __getitem__(self, index: int):
        return self._figures[index]

    def __str__(self):
        return f"{self._figures}"

    def __len__(self):
        return len(self._figures)

    def append(self, item: object):
        self._figures.append(item)

    def at(self, index: int):
        return self._figures[index]

    def remove(self, item: object):
        self._figures.remove(item)

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

    def load_figures(self, file_path: str, figure_factory):
        f = open(file_path, "r")
        while True:
            s = f.readline().strip()
            print("f.readline()", s)
            if not s:
                f.close()
                break
            figure = figure_factory.create_figure(s)
            figure.load(f, figure_factory)
            self._figures.append(figure)

    def save_figures(self, file_path: str):
        with open(file_path, "w") as f:
            for figure in self._figures:
                f.write(str(figure.save()))
