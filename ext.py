#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: ext.py
@time: 2019-04-11 17:24
"""


import pymysql
from const import HOSTNAME, USERNAME, PASSWD, DBNAME
from utils import singleton


@singleton
class create_orgin_engine():
    '''create mysql engine'''
    def __init__(self):
        self._engin = pymysql.connect(HOSTNAME, USERNAME, PASSWD, DBNAME)

    @property
    def engin(self):
        return self._engin

