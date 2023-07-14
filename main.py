import time

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# from hyper.contrib import HTTP20Adapter
from selenium.webdriver.chrome.service import Service # нужно для того чтобы передавать путь до драйвера
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver
from data_class import DataInfo
from set_driver import driver

from json import loads
import re


def get_sourse_html(url):
    driver.get(url)
    try:
        driver.get(url=url)
        driver.implicitly_wait(10)
        print(driver.window_handles)
        items = driver.find_elements(By.XPATH, '//div[@data-marker="item-photo"]')
        print(items)
        items[0].click()
        driver.switch_to.window(driver.window_handles[1])
        print(driver.current_url)
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        items[1].click()
        print(driver.current_url)
        time.sleep(4)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    get_sourse_html('https://www.avito.ru/all?q=%D0%BA%D1%80%D1%8B%D0%B6%D0%BE%D0%B2%D0%BD%D0%B8%D0%BA')