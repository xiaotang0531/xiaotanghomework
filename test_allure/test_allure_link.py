# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-12-09 19:48
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_allure_link.py
# @Software: PyCharm

import allure

@allure.link("http://www.baidu.com")
def test_link():
    pass