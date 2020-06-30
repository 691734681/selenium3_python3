#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")

element.send_keys("selenium")
sleep(3)

# 清除文本
element.clear()
sleep(3)

driver.quit()