#!/usr/bin/env python
# coding=utf-8

from url import url

import tornado.web
import os

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
    cookie_secret="dsEpo9M5Q3ue7q6nSmdWtg==",
    # xsrf_cookies=True,
    login_url=True,
    debug=True
)

application = tornado.web.Application(
    handlers=url,
    **settings
)
