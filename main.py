import random

from apps.data_operations.create_data import CreateData
import settings


__author__ = 'cenk'


def command(self, *args, **kwargs):
    print random.random()


if __name__ == "__main__":
    klass = CreateData(**{'log_active': settings.LOG, 'limit': settings.LIMIT})
    klass.write_to_csv()
