#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
title = driver.title
print(title)
url = driver.current_url
print(url)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)
num = driver.find_element_by_class_name("nums").text
print(num)
driver.quit()