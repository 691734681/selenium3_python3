#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
es = driver.find_elements_by_xpath('//*[@id="s-top-left"]/a')
for e in es:
	print(e.text)
driver.quit()