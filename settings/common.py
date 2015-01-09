import os

__author__ = 'cenk'

BASE_PATH = os.path.dirname(__file__)

DATA_PATH = os.path.join(BASE_PATH, '../data/data.csv')

LOG = True

LIMIT = 3000000
SLEEP_TIME = 0.01

CSV_HEADER = ['temos', 'start_date', 'end_date', 'time_delta', 'value']

USE_REDIS = True

REDIS_HOST = 'localhost'
REDIS_PORT = 6379