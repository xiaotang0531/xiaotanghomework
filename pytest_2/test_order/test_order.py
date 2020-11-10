# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 20:00
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_order.py
# @Software: PyCharm

import pytest

@pytest.mark.order(4)
def test_three():
    assert True

@pytest.mark.order(3)
def test_four():
    assert True

@pytest.mark.order(2)
def test_two():
    assert True

@pytest.mark.order(1)
def test_one():
    assert True