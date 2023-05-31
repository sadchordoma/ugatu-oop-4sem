from abc import ABC


# наблюдаемый
class Observable(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, _object):
        self._observers.append(_object)

    def notify_everyone(self):
        for observer in self._observers:
            observer.on_object_changed(self)
