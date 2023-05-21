from abc import ABC, abstractmethod


# наблюдатель
class Observer(ABC):
    @abstractmethod
    def on_object_changed(self, _object):
        pass
