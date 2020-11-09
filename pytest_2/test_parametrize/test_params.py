# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-08 21:35
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_params.py
# @Software: PyCharm
import os

import pytest
import yaml
from pytest import approx

from pytest_2.test_parametrize.calcu import Calculator



@pytest.fixture(autouse="true")
def creat_cal():
    calcu = Calculator()
    return calcu




class TestCalculator:

    @pytest.mark.dependency()
    @pytest.mark.parametrize('x, y, result',yaml.safe_load(open('data.yaml'))['add'])
    def check_add(self, creat_cal, x, y, result):
        print(f"{x} + {y} = {result}")
        assert creat_cal.add(x,y) == approx(result)



    @pytest.mark.dependency(name='mul')
    @pytest.mark.parametrize('x, y, result',yaml.safe_load(open('data.yaml'))['mul'])
    def checkmul(self, creat_cal, x, y, result):
        print(f"{x} * {y} = {result}")
        assert creat_cal.mul(x, y) == approx(result)


    @pytest.mark.dependency(depends=['mul'])
    @pytest.mark.parametrize('x, y, result',yaml.safe_load(open("data.yaml"))['div'])
    def testdiv(self, creat_cal, x, y, result):
        print(f"{x} / {y} = {result}")
        assert creat_cal.div(x, y) == approx(result)


    @pytest.mark.dependency(depends=['check_add'])
    @pytest.mark.parametrize('x, y, result',yaml.safe_load(open('data.yaml'))['sub'])
    def test_sub(self, creat_cal, x, y, result):
        print(f"{x} - {y} = {result}")
        assert creat_cal.sub(x, y) == approx(result)
