#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://localhost:8080/selenium_html/")
# frame = driver.find_element_by_name("aa")
# 切换表单可以使用 iframe的 id 或者 name
driver.switch_to.frame("aa")
driver.find_element_by_id("user").send_keys("selenium")
sleep(3)
# 切换回最外层 frame
driver.switch_to.default_content()
driver.find_element_by_id("user").send_keys("test")
sleep(3)
driver.quit()