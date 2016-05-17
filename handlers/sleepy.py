#!/usr/bin/env python
# coding=utf-8

from base import BaseHandler

import tornado.web
import time
import tornado.gen
import tornado.ioloop


class SleepHandler(BaseHandler):
    @tornado.web.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 17)
        #yield tornado.gen.sleep(17)
        self.render("sleep.html")


class SeeHandler(BaseHandler):
    def get(self):
        self.render("see.html")
