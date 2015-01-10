__author__ = 'cenk'


class Mean:
    def __init__(self):
        self.data = []

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self.data = [obj[index] for obj in data]
        else:
            self.data = data

        return self.__algorithm()

    def __algorithm(self):
        total = 0.0
        counter = 0
        for data in self.data:
            total += float(data)
            counter += 1
        try:
            return total / counter
        except ZeroDivisionError:
            print "integer division or modulo by zero"

