#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from functools import wraps
from statsd import StatsClient
from time import sleep

app = Flask(__name__)
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


@app.route("/login/<username>")
@Metric("view.login")
def login(username):
    if not username:
        statsd.incr("login.failed")
    sleep(1)
    statsd.incr("login.success")
    return "Hello World!"

if __name__ == "__main__":
    app.run()
