#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: app.py
@time: 2019-04-11 17:24
"""


from flask import Flask, redirect, url_for, render_template, request
from flask.views import MethodView
import mock
import upload_data
from ext import db
from utils import get_host_ip


app = Flask(__name__, static_folder='./static', template_folder='./template')
app.config.from_object('config')
db.init_app(app)


@app.route('/index/', methods=['GET'])
def index():
    return render_template('index_old.html', ip=get_host_ip())


@app.route('/', methods=['GET'])
def _index():
    return redirect(url_for('login_view'))


@app.errorhandler(404)
def not_found(error):
    return render_template('mock_error.html'),404


class UserAPI(MethodView):
    def get(self):
        return render_template("login.html")
    def post(self):
        if request.form['username'] == 'quanbing' and request.form['password'] == '123':
            return render_template('index_old.html', ip=get_host_ip(), user='quanbing')
        return "need login"

app.add_url_rule('/login', view_func=UserAPI.as_view('login_view'))
app.register_blueprint(mock.bp)
app.register_blueprint(upload_data.bp)


app.run(host='0.0.0.0', port=8989)
