from unittest import TestCase

from apps.csv.read_csv import ReadCsv
from apps.datasets.dataset import DataSet
import settings


__author__ = 'cenk'


class ImplementationTest(TestCase):
    def setUp(self):
        self.klass = ReadCsv(**{'log_active': settings.LOG})

    def test_create_dataset(self):
        self.klass.start()
        data, name = self.klass.get_data()
        dataset = DataSet()
        dataset.set(eval(data.get(name)))

        training_set, validation_set, test_set = dataset.split_train_validation_test_data()
        print dataset.get()
        print len(training_set.get()), training_set.get()
        print len(validation_set.get()), validation_set.get()
        print len(test_set.get()), test_set.get()
