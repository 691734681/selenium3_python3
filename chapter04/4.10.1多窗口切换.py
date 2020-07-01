#!/usr/local/python3.5/bin
# -*-  coding:utf-8 -*-

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://localhost:8080/selenium_html/")
handle1 = driver.current_window_handle
driver.find_element_by_link_text("Open new window").click()
sleep(5)
handles = driver.window_handles
for h in handles:
	if h == handle1:
		driver.switch_to.window(h)
sleep(5)
driver.quit()