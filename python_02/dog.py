# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 21:47
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : dog.py
# @Software: PyCharm


import animal

class Dog(animal.Animal):

    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.colour = kwargs['colour']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.hair = kwargs['hair']


    def shout(self):
        print(f'{self.name}会汪汪叫！')


    def watch_house(self):
        print(f'{self.name}会看家！')


    def __str__(self):
        print(f'狗狗的姓名--{self.name}，颜色--{self.colour}，年龄--{self.age}，性别--{self.gender}，毛发--{self.hair}！')