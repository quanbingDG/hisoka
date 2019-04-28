#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: mock.py
@time: 2019-04-11 17:25
"""

import os
from flask import Blueprint, redirect, url_for, jsonify, request
from config import mock_data_dir
from utils import load_hfsd, loads_hfsd


bp = Blueprint('mock', __name__, url_prefix='/mock')
global ic_dict, ec_dict
ic_dict, ec_dict = {}, {}


def check_param(queryString, param_list):
    '''
    @param queryString:
    @return:
    '''
    return all([queryString.__contains__(bytes(i, encoding='utf8')) for i in param_list])


@bp.route('/ic/', methods=['GET'])
def mock_ic():
    param_list = ['name', 'certno']
    if check_param(request.query_string, param_list = param_list):
        k = str(request.args.get('name')) + str(request.args.get('certno'))
        return jsonify(ic_dict[k]) if k in ic_dict.keys() else f"未找到对应的ic数据，{k}"
    else:
        return f"/mock/ic接口需要参数 {param_list} "


@bp.route('/ic/sample/', methods=['GET'])
def mock_ic_sample():
    return redirect(url_for('mock.mock_ic', name='陈XXX', certno='123456789987654320'))


@bp.route('/ec/', methods=['GET'])
def mock_ec():
    param_list = ['creditcode']
    if check_param(request.query_string, param_list = param_list):
        k = str(request.args.get('creditcode'))
        return jsonify(ec_dict[k]) if k in ec_dict.keys() else f"未找到对应的ec数据，creditcode : {k}"
    else:
        return f"/mock/ec接口需要参数 {param_list} "


@bp.route('/ec/sample/', methods=['GET'])
def mock_ec_sample():
    return redirect(url_for('mock.mock_ec', creditcode='123456788414140128'))


@bp.route('/sc/', methods=['GET'])
def mock_sc():
    pass


@bp.route('/reload/')
def data_reload():
    load_mock_data_hfsd()
    return jsonify({"message":"data reload success", "stats":200})


@bp.before_app_first_request
def load_mock_data_hfsd():
    print("starting....load data")

    for ic_data in loads_hfsd(mock_data_dir,'ic.hfsd'):
        k = ic_data.get('ICRHeader')[0].get('Name') + str(ic_data.get('ICRHeader')[0].get('Certno'))
        v = ic_data
        ic_dict[k] = v

    for ic_data in loads_hfsd(mock_data_dir,'ec.hfsd'):
        k = ic_data.get('ReportHeader')[0].get('CreditCode')
        v = ic_data
        ec_dict[k] = v

    print("finish....load data")