#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: ext.py
@time: 2019-04-11 17:24
"""


import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from const import HOSTNAME, USERNAME, PASSWD, DBNAME
from utils import singleton
from flask_sqlalchemy import SQLAlchemy


@singleton
class create_orgin_engine():
    '''create mysql engine'''
    def __init__(self):
        self._engin = pymysql.connect(HOSTNAME, USERNAME, PASSWD, DBNAME)

    @property
    def engin(self):
        return self._engin


@singleton
class create_sqlalchemy_engine():
    '''
    create mysql engine
    '''
    def __init__(self):
        pass
    engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWD, HOSTNAME, DBNAME),
                           encoding="utf-8", echo=False)
    Session = sessionmaker(bind=engine)
    _session = Session()

    @property
    def engin(self):
        return self._session


@singleton
class create_sqlalchemy_engine():
    '''
    create mysql engine
    '''
    def __init__(self):
        pass
    engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWD, HOSTNAME, DBNAME),
                           encoding="utf-8", echo=False)
    Session = sessionmaker(bind=engine)
    _session = Session()

    @property
    def engin(self):
        return self._session


db = SQLAlchemy()