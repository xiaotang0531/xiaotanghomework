# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-12-10 19:54
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_selenium.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testceshiren:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0)


    def teardown(self):
        self.driver.quit()


    def test_baidu_search(self):
        self.driver.get("http://www.baidu.com")

        self.driver.find_element_by_id("kw").send_keys("刘禹锡")
        self.driver.find_element_by_id("su").click()

        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="result c-container new-pmd"]')) >= 1

        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="result c-container new-pmd"]')))
        self.driver.find_element(By.XPATH,'//*[@mu="https://baike.baidu.com/item/刘禹锡/296467"]')
