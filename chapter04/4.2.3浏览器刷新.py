#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
sleep(3)

# 浏览器刷新
driver.refresh()
sleep(3)

driver.quit()