#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: app.py
@time: 2019-04-11 17:24
"""


from flask import Flask
import mock

app = Flask(__name__, static_folder='./static')
app.config.from_object('config')
app.register_blueprint(mock.bp)

import xmltodict,json

xmlfile = open(r'F:\项目文档\Plutus\03 个人征信标准化\征信2.0\九江项目\2代格式.xml', 'r', encoding='utf8')
xmlfile_ = xmlfile.read()
json_ = xmltodict.parse(xmlfile_)
print(json.dumps(json_, ensure_ascii=False))


# app.run(host='0.0.0.0', port=8989)
