import csv
import time

from apps.mocks.mock_data import MockData

from settings import DATA_PATH
from utils.logger import Logger


__author__ = 'cenk'


class WriteCsv(Logger):
    def __init__(self, *args, **kwargs):
        super(WriteCsv, self).__init__(**kwargs)
        self.path = kwargs['path'] if 'path' in kwargs   else DATA_PATH
        self.header = kwargs['header'] if 'header' in kwargs   else ['temos', 'start_date', 'end_date',
                                                                     'time_delta', 'value']
        self.limit = kwargs['limit'] if 'limit' in kwargs else 3000000
        self.sleep_time = kwargs['sleep_time'] if 'sleep_time' in kwargs  else 0.01
        self.data = kwargs['data'] if 'data' in kwargs  else MockData().default_data

    def write_to_csv(self, *args, **kwargs):
        with open(self.path, 'wb') as f:
            w = csv.DictWriter(f, fieldnames=self.header)
            try:
                counter = 0
                while counter < self.limit:
                    data = self.data()
                    w.writerow(data)
                    counter += 1
                    self.log(data)
                    time.sleep(self.sleep_time)
            except:
                raise
        f.close()