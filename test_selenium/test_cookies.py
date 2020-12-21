# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-12-18 20:08
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_cookies.py
# @Software: PyCharm
import json
from time import sleep

from selenium import webdriver


class TestCookies:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    def teardown(self):
        self.driver.quit()

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        with open("cookies.json","w") as f:
            json.dump(cookies,f)

    def test_cookies_login(self):
        # self.driver.add_cookie()
        cookies = json.load(open("cookies.json"))

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

        sleep(3)