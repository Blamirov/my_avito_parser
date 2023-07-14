import datetime
from loguru import logger
from set_driver import driver
import time
from datetime import datetime as dt
from random import randrange
from data_class import DataInfo
from selenium.webdriver.common.by import By
import re

months = {'января': '01', 'февраля': '02', 'марта': "03", 'апреля': '04', 'мая': '05', 'июня': '06', 'июля': '07',
          'августа': '08', 'сентября': '09', 'октября': "10", 'ноября': '11', 'декабря': '12'}


def get_data_info(driver, data):
    try:
        try:
            data.header = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text
        except Exception as ex:
            logger.error(f'Ошибка в заголовке {ex}\n curl = {driver.current_url}')
        try:
            data.price = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[3]/div[2]/'
                                                           'div[1]/div/div/div[1]/div/div/div/div[1]/div/span/span'
                                                           '/span[1]').text
        except Exception as ex:
            logger.error(f'Ошибка в цене {ex}\n curl = {driver.current_url}')
        try:
            driver.find_element(By.CLASS_NAME, 'style-item-price-discount-wrapper-Ltnye')
            data.down_price = 1
        except Exception as ex:
            data.down_price = 0

        try:
            views_total = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[3]/div['
                                              '1]/div[2]/div[4]/div/article/p/span[3]/span[1]').text
            data.views_total = re.search(r'\d*', views_total).group()
        except Exception as ex:
            logger.error(f'Ошибка в просмотрах итого {ex}\n curl = {driver.current_url}')
        try:
            views_today = driver.find_element(By.XPATH, '//span['
                                                        '@data-marker="item-view/today-views"]').text
            data.views_today = re.search(r'\d*', views_today[3:]).group()
        except Exception as ex:
            logger.error(f'Ошибка в просмотрах за сегодня {ex}\n curl = {driver.current_url}')

        data.method_promotions = 'Trying'

        try:
            refresh_time = driver.find_element(By.XPATH, '//span['
                                                         '@data-marker="item-view/item-date"]').text
            min_sec = re.search(r'\d{2}:\d{2}', refresh_time).group()
            if 'сегодня' in refresh_time:
                data.refresh_time = f'{datetime.datetime.today().strftime("%d.%m.%Y")} {min_sec}'
            else:
                day = re.search(r'\d{2}', refresh_time).group()
                month = re.search(r'[а-я]+', refresh_time).group()
                data.refresh_time = f'{day}.{months[month]}.{datetime.date.today().year} {min_sec}'
        except Exception as ex:
            logger.error(f'Ошибка во времени поднятия {ex}\n curl = {driver.current_url}')

        try:
            if driver.find_elements(By.XPATH, '//div[@data-marker="image-frame/image-wrapper"]'):
                data.amount_photo = 1 + len(driver.find_elements(By.XPATH, '//li[@data-marker="image-preview/item"]'))
            else:
                data.amount_photo = 0
        except Exception as ex:
            logger.error(f'Ошибка в количество фото {ex}\n curl = {driver.current_url}')

        try:
            data.text = driver.find_element(By.XPATH, '//div[@data-marker="item-view/item-description"]').text
        except Exception as ex:
            logger.error(f'Ошибка в тексте {ex}\n curl = {driver.current_url}')

        try:
            data.amount_signs = len(data.text)
        except Exception as ex:
            logger.error(f'Ошибка в количество знаков {ex}\n curl = {driver.current_url}')

        try:
            if driver.find_elements(By.XPATH, '//button[@data-marker="delivery-item-button-main"]'):
                data.delivery = 'Да'
            else:
                data.delivery = 'Нет'
        except Exception as ex:
            logger.error(f'Ошибка в доставке {ex}\n curl = {driver.current_url}')

        try:
            print(f'driver.windows = {driver.window_handles}')
            seller = driver.find_elements(By.XPATH, '//a[@data-marker="seller-link/link"]')
            if seller:
                seller[0].click()
                print(f'driver.windows_2 = {driver.window_handles}')
                driver.switch_to.window(driver.window_handles[2])
                data.seller_web = driver.current_url
                data.sellers_id = re.search(r'sellerId=.*', driver.current_url).group()[9:]
                driver.close()
                # driver.switch_to.window(driver.window_handles[1])
                print(f'window_handler_2 = {driver.window_handlers}')
            else:
                data.sellers_id = ''
                data.seller_web = ''
        except Exception as ex:
            logger.error(f'Ошибка в id продавца {ex}\n curl = {driver.current_url}')

        try:
            seller_name = driver.find_elements(By.CLASS_NAME, "styles-module-size_ms-EVWM")
            if seller_name:
                data.sellers_name = seller_name
            else:
                data.sellers_name = 'Частное лицо'
        except Exception as ex:
            logger.error(f'Ошибка в имени продавца {ex}\n curl = {driver.current_url}')

        try:
            data.announcements_id = driver.find_element(By.XPATH, '//span[@data-marker="item-view/item-id"]').text
        except Exception as ex:
            logger.error(f'Ошибка в id объявления {ex}\n curl = {driver.current_url}')

        try:
            data.active_announcements = None
        except Exception as ex:
            logger.error(f'Ошибка в активных объявлениях {ex}\n curl = {driver.current_url}')

        try:
            data.address = None
        except Exception as ex:
            logger.error(f'Ошибка в адресе {ex}\n curl = {driver.current_url}')

        try:
            data.web_link = driver.current_url
        except Exception as ex:
            logger.error(f'Ошибка в ссылка {ex}\n curl = {driver.current_url}')

        try:
            data.photo = None
        except Exception as ex:
            logger.error(f'Ошибка в фотографиях {ex}\n curl = {driver.current_url}')

        print(f'Заголовок: {data.header}\n'
              f'Цена: {data.price}\n'
              f'Понижение цены: {data.down_price}\n'
              f'Просмотры всего: {data.views_total}\n'
              f'Просмотры сегодня: {data.views_today}\n'
              f'Время поднятия:  {data.refresh_time}\n'
              f'Количество фотографий: {data.amount_photo}\n'
              f'Текст: {data.text[:10]}\n'
              f'Количество символов: {data.amount_signs}\n'
              f'Доставка: {data.delivery}\n'
              f'Id объявления: {data.announcements_id}\n'
              f'Id продавца: {data.sellers_id}\n'
              f'Ссылка на продавца {data.seller_web}\n'
              f'Имя продавца {data.sellers_name}\n'
              f'curl: {driver.current_url}')

    except Exception as ex:
        print(ex)

    finally:
        driver.close()


if __name__ == "__main__":
    pass