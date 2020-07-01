#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://localhost:8080/selenium_html/dragAndDrop.html")
e1 = driver.find_element_by_id("drag")
e2 = driver.find_element_by_tag_name("h1")
ActionChains(driver).drag_and_drop_by_offset(e1,400,400).perform()
sleep(3)
ActionChains(driver).drag_and_drop(e1,e2).perform()
sleep(3)
driver.quit()