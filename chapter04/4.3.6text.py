#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

element = driver.find_element_by_xpath("//*[@id='s-bottom-layer-right']/a/span")

res = element.text

print(res)

driver.quit()