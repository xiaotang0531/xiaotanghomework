#!/usr/bin/env python
# encoding: utf-8
# author: wb-tzh562887
# Creation time: 2020/11/6 10:13
# file name: test_calcu.py
# IDE: PyCharm

# pytest实战一作业
# 1、补全计算器（加减乘除）的测试用例
# 2、使用数据驱动完成测试用例的自动生成
# 3、conftest.py中创建fixture 完成setup和teardown
# 4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

import pytest
from pytest import approx
import yaml
import os

from cacu import Calculator

work_path = os.path.abspath(os.path.dirname(__file__))
testdata_file = os.path.join(work_path, 'data.yaml')
with open(testdata_file) as file:
    testdata = yaml.safe_load(file)

class TestCalcu:

    
    @pytest.mark.parametrize("x, y, result",testdata['add'])
    def test_add(self, creat_cal, x, y, result):
        print(f"{x}+{y}={result}")
        assert creat_cal.add(x, y) == approx(result)

   
    @pytest.mark.parametrize("x,y,result", testdata['sub'])
    def test_sub(self, creat_cal, x, y, result):
        print(f"{x}-{y}={result}")
        assert creat_cal.sub(x, y) == approx(result)

    
    @pytest.mark.parametrize("x,y,result", testdata['mul'])
    def test_mul(self, creat_cal, x, y, result):
        print(f"{x}*{y}={result}")
        assert creat_cal.mul(x, y) == approx(result)

    
    @pytest.mark.parametrize("x,y,result", testdata['div'])
    def test_div(self, creat_cal, x, y, result):
        print(f"{x}/{y}={result}")
        assert creat_cal.div(x, y) == approx(result)