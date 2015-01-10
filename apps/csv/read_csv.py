import csv

from apps.redis.redis_instance import Redis

from settings import DATA_PATH, INTERFACE_NAME
import settings
from utils.logger import Logger


__author__ = 'cenk'


class ReadCsv(Logger):
    def __init__(self, *args, **kwargs):
        super(ReadCsv, self).__init__(**kwargs)
        self.path = kwargs['path'] if 'path' in kwargs   else DATA_PATH
        self.interface_name = kwargs['interface_names'] if 'interface_names' in kwargs  else INTERFACE_NAME
        self.interface_maping = {}
        self.redis_used = False

    def start(self, *args, **kwargs):
        with open(self.path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            interface_mapping = {}
            interface_data = []
            for row in spamreader:
                interface_data.append((row[3], row[4]))
            try:
                if settings.USE_REDIS:
                    self.redis_used = True
                    redis_connection = Redis.get_connection()
                    for interface in interface_mapping:
                        redis_connection.set(self.interface_name, interface_data)
                else:
                    raise
            except:
                interface_mapping[self.interface_name] = str(interface_data)
                self.interface_maping = interface_mapping
            self.log(interface_mapping)
        csvfile.close()

    def get_data(self):
        if self.redis_used:
            return Redis.get_connection(), self.interface_name

        return self.interface_maping, self.interface_name



