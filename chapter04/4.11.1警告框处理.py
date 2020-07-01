#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://localhost:8080/selenium_html/")
driver.maximize_window()
sleep(5)
# alert框
e = driver.find_element_by_id("alert")
e.click()
sleep(5)
alert = driver.switch_to.alert
# driver.switch_to.alert.accept()
# sleep(5)
# # confirm框
# driver.find_element_by_id("confirm").click()
# sleep(5)
# driver.switch_to.alert.dismiss()
# sleep(5)
# # prompt
# driver.find_element_by_id("prompt").click()
# sleep(5)
# driver.switch_to.alert.send_keys("test")
# sleep(5)
# driver.switch_to.alert.accept()
# sleep()
driver.quit()
