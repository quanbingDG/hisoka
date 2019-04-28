#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: upload_data.py
@time: 2019-04-27 16:14
"""


from flask import Blueprint, render_template, request
import magic
import os
from flask import current_app
from sys import getsizeof
import json
from models import ICR, ECR
from ext import db
from utils import get_file_path, hash_filename, get_file_md5


bp = Blueprint('upload', __name__, url_prefix='/upload')


@bp.route('/', methods=['GET'])
def upload():
    return render_template('upload.html')


@bp.route('/ic/', methods=['POST'])
def upload_ic():
    upload_file = request.files['file']
    file_path = get_file_path(hash_filename(upload_file.filename))
    upload_file.save(file_path)
    with open(file_path, 'rb') as f:
        for line in f:
            filemd5 = get_file_md5(line)
            uploaded_file = ICR.get_file_bymd5(filemd5)
            if not uploaded_file:
                _tmp = json.loads(line)
                Name = _tmp.get('ICRHeader')[0].get('Name')
                Certno = _tmp.get('ICRHeader')[0].get('Certno')
                icr = ICR(Name=Name, Cert_no=Certno, File_content=line, Size=getsizeof(line), File_md5=filemd5)
                db.session.add(icr)
                db.session.commit()
    return "IC Data Upload Success!"


@bp.route('/ec/', methods=['POST'])
def upload_ec():
    upload_file = request.files['file']
    file_path = get_file_path(hash_filename(upload_file.filename))
    upload_file.save(file_path)
    with open(file_path, 'rb') as f:
        for line in f:
            filemd5 = get_file_md5(line)
            uploaded_file = ECR.get_file_bymd5(filemd5)
            if not uploaded_file:
                _tmp = json.loads(line)
                creditcode = _tmp.get('ReportHeader')[0].get('CreditCode')
                ecr = ECR(creditcode = creditcode, File_content=line, Size=getsizeof(line), File_md5=filemd5)
                db.session.add(ecr)
                db.session.commit()
    return "EC Data Upload Success!"
