#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("http://localhost:8080/selenium_html/")

element = driver.find_element_by_id("user")

element.send_keys("selenium_webdriver")
# 鼠标双击
ActionChains(driver).double_click(element).perform()
sleep(3)

driver.quit()