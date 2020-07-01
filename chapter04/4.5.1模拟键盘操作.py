#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost:8080/selenium_html/")
e = driver.find_element_by_id("user")
e.send_keys("selenium")
e.send_keys(Keys.BACK_SPACE)
sleep(3)
e.send_keys(Keys.CONTROL,'a')
sleep(3)
driver.quit()