#!/usr/bin/env python
# encoding: utf-8
# author: wb-tzh562887
# Creation time: 2020/11/6 10:21
# file name: conftest.py
# IDE: PyCharm
import pytest

from cacu import Calculator


@pytest.fixture(autouse="true")
def creat_cal():
    print("开始计算：")
    cal = Calculator()
    yield cal

    print("计算结束！")
