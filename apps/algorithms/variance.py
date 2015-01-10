from apps.algorithms.mean import Mean

from apps.algorithms.sum_formula import SumFormula


__author__ = 'cenk'


class Variance:
    def __init__(self):
        self.data = []
        self.n = 0

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self.data = sorted([obj[index] for obj in data])
        else:
            self.data = sorted(data)
        self.n = len(self.data)
        return self.__algorithm()


    def __algorithm(self):
        mean = Mean()
        mean_value = mean.calculate(self.data)
        values = map(lambda x: (float(x) - mean_value), self.data)
        sum_formula = SumFormula()
        sum_of_powers = sum_formula.calculate(values, power=2)

        result = sum_of_powers / (self.n - 1)

        try:
            return round(result, 4)
        except:
            print ""