#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        usernames = mrd.select_columns(table="authors", column="name")
        one_user = usernames[1][0]
        self.render("index1.html", user=one_user)


    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        # self.write({"usr": username, "pass": password})
        user_infos = mrd.select_table(table="authors", column="*", condition="name", value=username)
        if user_infos:
            db_pwd = user_infos[0][3]
            if db_pwd == password:
                self.set_current_user(username)
                self.write(username)
            else:
                self.write("-1")
        else:
            self.write("-1")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")


