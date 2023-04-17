class Model:
    def __init__(self):
        self.__value_a = 0
        self.__value_b = 0
        self.__value_c = 0

        self.observers = []

        self.open_data()

    def open_data(self):
        with open("saved_data.txt") as f:
            s = f.read()
            if len(s) > 0:
                a, b, c = map(int, s.split(" "))
                self.__value_a = a
                self.__value_b = b
                self.__value_c = c
                self.notify()

    def save_data(self):
        with open("saved_data.txt", "w") as f:
            s = " ".join(str(item) for item in self.get_values_all())
            f.write(s)

    def __del__(self):
        self.save_data()

    def notify(self):
        for o in self.observers:
            o.event_generate("<<UpdateForm>>")

    def get_value_a(self):
        return self.__value_a

    def get_value_b(self):
        return self.__value_b

    def get_value_c(self):
        return self.__value_c

    def get_values_all(self):
        return [self.__value_a, self.__value_b, self.__value_c]

    def set_value_a(self, value):
        try:
            value = int(value)
        except ValueError:
            pass
        else:
            if value < 0:
                self.__value_a = 0
            else:
                # take user input and correct other values
                if value > 100:
                    self.__value_a = 100
                else:
                    self.__value_a = value
                if self.__value_a > self.__value_b:
                    self.__value_b = self.__value_a
                    if self.__value_b > self.__value_c:
                        self.__value_c = self.__value_b
            # call update form
        finally:
            self.notify()

    def set_value_b(self, value):
        # prohibition behaviour
        try:
            value = int(value)
        except ValueError:
            pass
        else:
            if self.__value_a <= value <= self.__value_c:
                self.__value_b = value
            # call update form
        finally:
            self.notify()

    def set_value_c(self, value):
        try:
            value = int(value)
        except ValueError:
            pass
        else:
            if value < 0:
                self.__value_c = 0
            else:
                # take user input and correct other values
                if value > 100:
                    self.__value_c = 100
                else:
                    self.__value_c = value
                if self.__value_c < self.__value_b:
                    self.__value_b = self.__value_c
                    if self.__value_b < self.__value_a:
                        self.__value_a = self.__value_b
            # call update form
        finally:
            self.notify()
