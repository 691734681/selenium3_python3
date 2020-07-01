#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.quit()