#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: app.py
@time: 2019-04-11 17:24
"""


from flask import Flask, redirect, url_for, render_template
import mock
import upload_data
from ext import db


app = Flask(__name__, static_folder='./static', template_folder='./template')
app.config.from_object('config')
db.init_app(app)


@app.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def _index():
    return redirect(url_for('index'))File_md5


@app.errorhandler(404)
def not_found(error):
    return render_template('mock_error.html'),404


app.register_blueprint(mock.bp)
app.register_blueprint(upload_data.bp)


app.run(host='0.0.0.0', port=8989)
