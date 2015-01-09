import random

__author__ = 'cenk'


class DataSet:
    def __init__(self):
        self._data = None

    def set(self, data, extend=False):
        """
        Sets data to the dataset

        :param data: a list of tuples
        :type data: list
        """
        if extend:
            self._data.extend(data)
        else:
            self._data = data

    def get(self):
        """
        :returns: a list of tuples
        """
        return self._data

    def split_train_validation_test_data(self, percent=(60, 20, 20), shuffle_data=True):
        if shuffle_data:
            random.shuffle(self._data)
        length = len(self._data)
        train_list = self._data[:int(round(length * percent[0] / 100.0))]
        validation_list = self._data[
                          int(round(length * percent[0] / 100.0)):int(
                              round(length * (percent[0] + percent[1]) / 100.0))]
        test_list = self._data[-int(round(length * ( percent[2]) / 100.0)):]

        train = DataSet()
        train.set(train_list)
        validation = DataSet()
        validation.set(validation_list)
        test = DataSet()
        test.set(test_list)

        return train, validation, test