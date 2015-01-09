import redis

from settings import REDIS_HOST, REDIS_PORT


__author__ = 'cenk'


class Redis:
    @staticmethod
    def get_connection():
        return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)