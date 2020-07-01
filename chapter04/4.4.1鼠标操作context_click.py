#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("http://localhost:8080/selenium_html/")

element = driver.find_element_by_id("user")

# 通过ActionChains调用driver完成鼠标操作，所有鼠标操作最后必须调用perform方法
# context_click()是鼠标右击
ActionChains(driver).context_click(element).perform()
sleep(3)

driver.quit()