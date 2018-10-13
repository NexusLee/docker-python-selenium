# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class WithoutOpenId():
    def test():
        driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)

        print('==================无openid进入==================')
        driver.get("http://www.example.com")
        html = driver.page_source
        print(html)
        sleep(3)
        driver.get_screenshot_as_file("/app/result/no-openid.png")

        driver.quit()

