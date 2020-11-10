# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 21:36
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : animal.py
# @Software: PyCharm

class Animal:


    def __init__(self,name,colour,age,gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender



    def run(self):
        print('动物会跑！')


    def shout(self):
        print('动物会叫！')