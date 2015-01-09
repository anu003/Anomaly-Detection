__author__ = 'cenk'


class Logger(object):
    def __init__(self, *args, **kwargs):
        self.log_active = 'log_active' in kwargs and kwargs['log_active']

    def log(self, obj, *args, **kwargs):
        if self.log_active:
            print obj