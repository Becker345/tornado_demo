#!/usr/bin/env python
# coding=utf-8

import MySQLdb

conn = MySQLdb.Connect(host="localhost", user="root", passwd="inspur8", db="blog", port=3306)
cur = conn.cursor()
