from unittest import TestCase

from apps.csv.read_csv import ReadCsv


__author__ = 'cenk'


class ReadDataTest(TestCase):
    def test_read_data_from_csv(self):
        klass = ReadCsv()
        klass.start()
