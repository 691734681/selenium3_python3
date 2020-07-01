#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://localhost:8080/selenium_html/")
e = driver.find_element_by_id("over")
# 鼠标悬停
ActionChains(driver).move_to_element(e).perform()
sleep(3)
driver.quit()