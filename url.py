#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""

import sys

reload(sys)

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.sleepy import SleepHandler, SeeHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/see', SleepHandler),
    (r'/sleep', SeeHandler)
]
