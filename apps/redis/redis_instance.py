import redis

__author__ = 'cenk'


class Redis:
    @staticmethod
    def get_connection():
        return redis.StrictRedis(host='localhost', port=6379, db=0)