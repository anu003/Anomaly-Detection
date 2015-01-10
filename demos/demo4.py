import os

from apps.algorithms.mean import Mean
from apps.algorithms.standart_deviation import StandartDeviation
from apps.algorithms.z_value import ZValue
from apps.csv.read_csv import ReadCsv
from apps.data_operations.create_data import CreateData
from apps.datasets.dataset import DataSet
from settings import BASE_PATH


__author__ = 'cenk'


def demo4():
    path = os.path.join(BASE_PATH, '../data/demo4.csv')
    klass = CreateData(**{'log_active': False, 'limit': 10000, 'path': path})
    klass.start()
    klass = ReadCsv(**{'log_active': False, 'path': path})
    data, name = klass.get_data()
    dataset = DataSet()
    dataset.set(data.get(name))
    train, validation, test = dataset.split_train_validation_test_data()
    training_list = train.get()
    validation_list = validation.get()
    test_list = test.get()
    standart_deviation = StandartDeviation()
    standart_deviation_value = standart_deviation.calculate(training_list)
    mean = Mean()
    mean_value = mean.calculate(training_list)
    # print "Training Set: %s, Validation Set: %s, Test Set: %s" % (training_list, validation_list, test_list)
    print "Standart Deviation: %f, Mean Value: %f" % (standart_deviation_value, mean_value)
    z_value = ZValue()
    for val in validation_list:
        z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value)
        table_value = z_value.find_from_table()
        if table_value == -1:
            print "This val is anomaly:", val
    for val in test_list:
        z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value)
        table_value = z_value.find_from_table()
        if table_value == -1:
            print "This val is anomaly:", val