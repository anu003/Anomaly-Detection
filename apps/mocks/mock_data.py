import random
from datetime import datetime, timedelta

from apps.random.randoms import Randoms
from utils.logger import Logger


__author__ = 'cenk'


class MockData(Logger):
    def default_data(self, *args, **kwargs):
        interface = Randoms.random_from_list(['a', 'b', 'c'])
        sleep_time = random.randint(1, 10)
        data = {}
        start_date = datetime.now()
        end_date = datetime.now() + timedelta(seconds=sleep_time)
        data['temos'] = interface
        data['value'] = Randoms.random_with_probability() * sleep_time
        data['start_date'] = start_date.strftime("%Y-%m-%d %H:%M %S")
        data['end_date'] = end_date.strftime("%Y-%m-%d %H:%M %S")
        data['time_delta'] = (end_date - start_date).seconds
        self.log(data)
        return data