# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-12-07 20:52
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_allure.py
# @Software: PyCharm


import allure



@allure.feature("login")
def test_login():
    with allure.step("输出print"):
        print("这是登录测试")
    with allure.step("断言"):
        assert 1 + 1 == 2


@allure.feature("login")
def test_login1():
    with allure.step("输出print"):
        print("这是登录测试")
    with allure.step("断言"):
        assert 2 + 3 == 2

@allure.feature("add")
def test_add():
    with allure.step("输出print"):
        print("这是加法测试")
    with allure.step("断言"):
        assert 1 + 1 == 2


@allure.feature("sub")
def test_sub():
    with allure.step("断言"):
        assert 2 - 1 == 1
    with allure.step("输出print"):
        print("这是登录测试")

