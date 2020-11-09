#!/usr/bin/env python
# encoding: utf-8
# author: wb-tzh562887
# Creation time: 2020/11/6 10:47
# file name: calcu.py
# IDE: PyCharm
# Filename : test.py
# author by : www.runoob.com

class Calculator:

    @classmethod
    def add(cls, x, y):
        return x + y

    @classmethod
    def sub(cls, x, y):
        return x - y

    @classmethod
    def mul(cls, x, y):
        return x * y

    @classmethod
    def div(cls, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return False
