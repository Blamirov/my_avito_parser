import time

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# from hyper.contrib import HTTP20Adapter
from selenium.webdriver.chrome.service import Service  # нужно для того чтобы передавать путь до драйвера
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from data_class import DataInfo
from method_promotions import get_method_promotions
from set_driver import driver
from random import randrange
from json import loads
import re
from data_class import DataInfo
from get_info_announcenent import get_data_info


def get_items(url):
    driver.get(url)
    time.sleep(randrange(3, 10))
    try:
        for i in range(2):
            item = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
            for announcement in item:
                data_ann = DataInfo()
                get_method_promotions(driver, data_ann)
                announcement.click()
                driver.switch_to.window(driver.window_handles[1])
                get_data_info(driver, data_ann)

                driver.switch_to.window(driver.window_handles[0])
                time.sleep(randrange(3, 10))
                print(f'Заголовок: {data_ann.header}\n'
                      f'Цена: {data_ann.price}\n'
                      f'Понижение цены: {data_ann.down_price}\n'
                      f'Просмотры всего: {data_ann.views_total}\n'
                      f'Просмотры сегодня: {data_ann.views_today}\n'
                      f'Время поднятия:  {data_ann.refresh_time}\n'
                      f'Количество фотографий: {data_ann.amount_photo}\n'
                      f'Текст: {data_ann.text[:10]}\n'
                      f'Количество символов: {data_ann.amount_signs}\n'
                      f'Доставка: {data_ann.delivery}\n'
                      f'Id объявления: {data_ann.announcements_id}\n'
                      f'Id продавца: {data_ann.sellers_id}\n'
                      f'Ссылка на продавца {data_ann.seller_web}\n'
                      f'Имя продавца {data_ann.sellers_name}\n'
                      f'curl: {driver.web_link}')

            next_page = driver.find_elements(By.XPATH,
                                             '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div[3]/div[3]/nav/ul/li[7]/a')

            next_page[0].click()
            time.sleep(randrange(3, 10))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        print('сбор items закончен')


if __name__ == "__main__":
    my_items = get_items('https://www.avito.ru/sankt-peterburg/odezhda_obuv_aksessuary/obuv_zhenskaya-ASgBAgICAUTeAryp1gI?cd=1')
