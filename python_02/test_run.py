# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 22:07
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_run.py
# @Software: PyCharm

import yaml
from cat import Cat
from dog import Dog

attribute = yaml.safe_load(open('animal.yml'))


cat = Cat(attribute['cat'])






cat.catching_mice()
cat.__str__()


dog = Dog(attribute['dog'])
dog.watch_house()
dog.__str__()