#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")

element.send_keys("seleinum")

# 提交表单
element.submit()

driver.quit()