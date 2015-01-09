import csv

from apps.redis.redis_instance import Redis

from settings import DATA_PATH
import settings
from utils.logger import Logger


__author__ = 'cenk'


class ReadCsv(Logger):
    def __init__(self, *args, **kwargs):
        super(ReadCsv, self).__init__(**kwargs)
        self.path = kwargs['path'] if 'path' in kwargs   else DATA_PATH
        self.interface_names = []
        self.interface_maping = {}

    def start(self, *args, **kwargs):
        with open(self.path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            interface_mapping = {}
            for row in spamreader:

                if not row[0] in interface_mapping:
                    interface_mapping[row[0]] = []
                    self.interface_names.append(row[0])
                interface_mapping[row[0]].append((row[3], row[4]))
            try:
                if settings.USE_REDIS:
                    redis_connection = Redis.get_connection()
                    for interface in interface_mapping:
                        redis_connection.set(interface, interface_mapping[interface])
                else:
                    raise
            except:
                self.interface_maping = interface_mapping

        csvfile.close()

