#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_link_text("hao123")

# 单击元素
element.click()
sleep(5)

driver.quit()