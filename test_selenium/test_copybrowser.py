# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-12-18 19:55
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_copybrowser.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCopyBrowser:

    def setup(self):
        option = Options()
        option.debugger_address = 'localhost:9494'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)


    def teardown(self):
        pass

    def test_copybrowser(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#indexTop a:nth-child(1)').click()
