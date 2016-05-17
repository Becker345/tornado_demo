#!/usr/bin/env python
# coding=utf-8

import tornado.web
import methods.readdb as mrd


class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        user_infos = mrd.select_table(table="authors", column="*", condition="name", value=username)
        self.render("user.html", users=user_infos)
