# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 20:25
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_order1.py
# @Software: PyCharm

import pytest_ordering

import pytest

@pytest.mark.run(order=2)
def test_three():
    assert True

@pytest.mark.run(order=1)
def test_four():
    assert True

@pytest.mark.run(order=3)
def test_two():
    assert True

@pytest.mark.run(order=4)
def test_one():
    assert True