#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: models.py
@time: 2019-04-27 16:06
"""

from ext import db
from datetime import datetime
from flask import abort


class ICR(db.Model):
    __tablename__ = 'icr_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(512), nullable=False)
    Cert_no = db.Column(db.String(128), nullable=False)
    File_content = db.Column(db.Text, nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    File_md5 = db.Column(db.String(255), nullable=False)
    Upload_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, Name, Cert_no, File_content, File_md5, Size):
        self.Name = Name
        self.Cert_no = Cert_no
        self.File_content = File_content
        self.Upload_time = datetime.now()
        self.File_md5 = File_md5
        self.Size = Size


    @classmethod
    def get_file_bymd5(cls,file_md5):
        return cls.query.filter_by(File_md5=file_md5).first()


class ECR(db.Model):
    __tablename__ = 'ecr_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creditcode = db.Column(db.String(512), nullable=False)
    File_content = db.Column(db.Text, nullable=False)
    Upload_time = db.Column(db.DateTime, nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    File_md5 = db.Column(db.String(255), nullable=False)

    def __init__(self, creditcode, File_content, Size, File_md5):
        self.creditcode = creditcode
        self.File_content = File_content
        self.Upload_time = datetime.now()
        self.Size = Size
        self.File_md5 = File_md5

    @classmethod
    def get_file_bymd5(cls, file_md5):
        return cls.query.filter_by(File_md5=file_md5).first()