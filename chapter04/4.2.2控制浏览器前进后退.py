#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
sleep(3)

driver.get("http://www.sogou.com")
sleep(3)

# 浏览器回退
driver.back()
sleep(3)

# 浏览器前进
driver.forward()
sleep(3)

driver.quit()
