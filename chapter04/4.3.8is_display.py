#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_id("kw")

res = element.is_displayed()

print(res)

driver.quit()
