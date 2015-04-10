#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from statsd import StatsClient
from time import sleep

statsd = StatsClient('127.0.0.1', 8125)

class Metric(object):

    def __init__(self, metric):
        self.metric = metric

    def __call__(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            with statsd.timer(self.metric):
                return f(*args, **kwargs)
        return decorated

@Metric("test")
def test():
   sleep(5)


if __name__ == '__main__':
    test()
