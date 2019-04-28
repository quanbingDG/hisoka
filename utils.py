#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: quanbing
@file: utils.py
@time: 2019-04-11 18:11
"""

import json
import os
import uuid
import socket
from functools import partial
from const import UPLOAD_DIR
import hashlib


HERE = os.path.abspath(os.path.dirname(__file__))
get_file_path = partial(os.path.join, HERE, UPLOAD_DIR)


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


def hash_filename(filename):
    _, _, suffix = filename.rpartition('.')
    return '{0}.{1}'.format(uuid.uuid4().hex, suffix)


def get_file_md5(f):
    h = hashlib.md5()
    while True:
        if not f:
            break
        h.update(f)
        return h.hexdigest()


def get_file_size(bytesize, precision=2):
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'bytes')
    )
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    return '%.*f %s' % (precision, bytesize / factor, suffix)


def get_host_ip():
    """
    get the host ip
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip