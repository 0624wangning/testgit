#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-20 11:41
# @Author  : wangning
from selenium import webdriver
from time import sleep

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'}
    # desired_capabilities={'browserName': 'firefox'}
)
driver.get('https://www.baidu.com')
print("get baidu")

driver.find_element_by_id("kw").send_keys("docker selenium")
driver.find_element_by_id("su").click()
sleep(1)
driver.get_screenshot_as_file("/tmp/screenshot/baidu_img.png")
driver.quit()