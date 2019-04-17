#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: utils.py
@time: 2019-04-11 18:11
"""

import json
import os


def write_txt():
    pass


def load_hfsd(abs_file_path, file_name):
    return [json.load(open(os.path.join(abs_file_path, file_name), encoding='utf8'))]


def loads_hfsd(abs_file_path, file_name):
    '''
    :param abs_file_path:
    :param file_name:
    :return:
    '''
    result = []
    with open(os.path.join(abs_file_path, file_name), encoding='utf8') as f:
        for line in f:
            result.append(json.loads(line))
    return result


def check_parme_wrapper(args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            param_num = func.__code__.co_argcount
            param_list = func.__code__.co_varnames
            for arg in args:
                if arg in param_list:
                    pass
        return wrapper
    return decorator



