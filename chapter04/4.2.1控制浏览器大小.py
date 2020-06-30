#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
sleep(5)

# 控制浏览器尺寸
driver.set_window_size(480,800)
sleep(5)

# 浏览器最大化
driver.maximize_window()
sleep(5)

# 退出driver
driver.quit()
