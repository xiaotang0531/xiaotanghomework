# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 20:24
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_env.py
# @Software: PyCharm

import pytest
import yaml


def pytest_addoption(parser):
    mygroup = parser.getgroup("Env")
    mygroup.addoption('--env',
                     default='test',
                     dest='env',
                     help='set your run env!')


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default='test')
    if myenv == 'test':
        with open('datas/testdata.yml') as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        with open('datas/devdata.yml') as f:
            datas = yaml.safe_load(f)

    return datas
