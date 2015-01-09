import csv
from datetime import datetime, timedelta
import time
import random

from apps import DATA_PATH


__author__ = 'cenk'


class CreateData:
    def log(self, obj):
        if self.log_active:
            print obj

    def __init__(self, **kwargs):

        self.log_active = 'log_active' in kwargs and kwargs['log_active']
        self.path = kwargs['path'] if 'path' in kwargs   else DATA_PATH
        self.limit = kwargs['limit'] if 'limit' in kwargs else 3000000
        self.header = kwargs['header'] if 'header' in kwargs   else ['temos', 'start_date', 'end_date',
                                                                     'time_delta', 'value']
        self.data = kwargs['data'] if 'data' in kwargs  else self.default_data
        self.sleep_time = kwargs['sleep_time'] if 'sleep_time' in kwargs  else 0.01

    def default_data(self):
        interface = self.get_random_from_list(['a', 'b', 'c'])
        sleep_time = random.randint(0, 10)
        data = {}
        start_date = datetime.now()
        end_date = datetime.now() + timedelta(seconds=sleep_time)
        data['temos'] = interface
        data['value'] = self.get_random() * sleep_time
        data['start_date'] = start_date.strftime("%Y-%m-%d %H:%M %S")
        data['end_date'] = end_date.strftime("%Y-%m-%d %H:%M %S")
        data['time_delta'] = (end_date - start_date).seconds
        self.log(data)
        return data

    def write_to_csv(self):
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

    def get_random(self):
        percent = random.random()
        if percent > 0.05:
            return random.randint(1000, 10000000)
        else:
            return random.randint(0, 1000)

    def get_random_from_list(self, string_list):
        return random.choice(string_list)

    def command(self):
        print random.random()


