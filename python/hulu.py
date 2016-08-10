# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()


def is_alert_present(driver):
    try:
        driver.switch_to_alert().text
        return True
    except:
        return False


def login():
    driver.get('https://secure.hulu.jp/login')

    loginIdInput = driver.find_element_by_id('login')
    loginIdInput.click()
    loginIdInput.clear()
    loginIdInput.send_keys('mailaddress')

    loginPasswordInput = driver.find_element_by_id('password')
    loginPasswordInput.click()
    loginPasswordInput.clear()
    loginPasswordInput.send_keys('password')

    driver.find_element_by_xpath('//div[@class="btn-center"]').click()


def access_godzilla_movie(url):
    driver.get(url)
    time.sleep(10)
    count = 0
    while(count < 10):
        driver.save_screenshot('godzilla' + str(count) + '.jpg')
        time.sleep(1)
        count += 1


def main():
    try:
        login()
        access_godzilla_movie('http://www.hulu.jp/watch/948895')


    finally:
        driver.close()
        if not success:
            raise Exception('Test failed.')


main()
