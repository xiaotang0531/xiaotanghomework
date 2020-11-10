# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-10 21:37
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : cat.py
# @Software: PyCharm


import animal

class Cat(animal.Animal):

    def __init__(self,kwargs):
        self.name = kwargs['name']
        self.colour = kwargs['colour']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.hair = kwargs['hair']


    def shout(self):
        print(f"{self.name}会喵喵叫！")


    def catching_mice(self):
        print(f'{self.name}会捉老鼠！')

    def __str__(self):
        print(f'猫猫的姓名--{self.name}，颜色--{self.colour}，年龄--{self.age}，性别--{self.gender}，毛发--{self.hair}捉到老鼠了！')