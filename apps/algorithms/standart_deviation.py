import math

from apps.algorithms.variance import Variance


__author__ = 'cenk'


class StandartDeviation:
    def __init__(self):
        self.data = []

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self.data = sorted([obj[index] for obj in data])
        else:
            self.data = sorted(data)

        return self.__algorithm()

    def __algorithm(self):
        variance = Variance()
        return round(math.pow(variance.calculate(self.data), 0.5), 4)