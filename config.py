#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: config.py
@time: 2019-04-11 17:54
"""
from const import HOSTNAME, DBNAME, USERNAME, PASSWD

mock_data_dir = './data'
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWD, HOSTNAME, DBNAME)
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
