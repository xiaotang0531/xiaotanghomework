# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-12-07 20:52
# @Author : xiaotang
# @Email : xiaotang0531@163.com
# @File : test_allure.py
# @Software: PyCharm
import allure
import pytest
import time
from selenium import webdriver



@allure.feature("百度搜索功能")
@pytest.mark.parametrize("test_data",['李白','李煜','李商隐','杜甫','刘禹锡'])
def test_bdseach_demo(test_data):

    with allure.step("打开浏览器进入百度"):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.maximize_window()

    with allure.step(f"输入测试数据:{test_data}"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)

    with allure.step("点击搜索"):
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存搜索结果"):
        driver.save_screenshot("./result/Mr.jpg")
        allure.attach.file("./result/Mr.jpg", attachment_type=allure.attachment_type.JPG)

    with allure.step("关闭浏览器"):
        driver.quit()



