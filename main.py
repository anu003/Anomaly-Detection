from apps.algorithms.mean import Mean

from apps.algorithms.standart_deviation import StandartDeviation
from apps.algorithms.z_value import ZValue

from apps.csv.read_csv import ReadCsv

from apps.data_operations.create_data import CreateData
from apps.datasets.dataset import DataSet
import settings


__author__ = 'cenk'


def main():
    write_klass = CreateData(**{'log_active': settings.LOG, 'limit': settings.LIMIT})
    write_klass.start()

    read_klass = ReadCsv(**{'log_active': settings.LOG})
    read_klass.start()
    data, name = read_klass.get_data()
    dataset = DataSet()
    dataset.set(eval(data.get(name)))
    train, validation, test = dataset.split_train_validation_test_data()
    training_list = train.get()
    validation_list = validation.get()
    test_list = test.get()

    standart_deviation = StandartDeviation()
    standart_deviation_value = standart_deviation.calculate(training_list)
    mean = Mean()
    mean_value = mean.calculate(training_list)
    print standart_deviation_value, mean_value
    z_value = ZValue()
    for val in test_list:
        z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value)
        table_value = z_value.find_from_table()
        if table_value != -1:
            "Print it's normal"
        else:
            print "This val is anomaly: %f" % val


if __name__ == "__main__":
    main()
