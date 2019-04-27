#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: utils.py
@time: 2019-04-11 18:11
"""

import json
import os


def write_txt(filename='test.csv', info='', mode='a'):
    '''
    写入txt文本文档
    参数：
        filename：文件路径
        info：写入信息
        mode:
            r 只能读
            r+ 可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
            w+ 可读可写 如果文件存在 则覆盖整个文件不存在则创建
            w 只能写 覆盖整个文件 不存在则创建
            a 只能写 从文件底部添加内容 不存在则创建
            a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
    '''
    f = open(filename, mode=mode + r"\n")
    try: f.writelines(info)
    finally: f.close()


def load_hfsd(abs_file_path, file_name):
    '''
    :param abs_file_path:
    :param file_name:
    :return: a list
    '''
    return [json.load(open(os.path.join(abs_file_path, file_name), encoding='utf8'))]


def loads_hfsd(abs_file_path, file_name):
    '''
    :param abs_file_path:
    :param file_name:
    :return: a dict
    '''
    result = []
    with open(os.path.join(abs_file_path, file_name), encoding='utf8') as f:
        for line in f:
            result.append(json.loads(line))
    return result


def singleton(cls):
    '''
    :param cls: a derector to implement singleton cls
    '''
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
            return _instance[cls]
        return _instance[cls]
    return _singleton


