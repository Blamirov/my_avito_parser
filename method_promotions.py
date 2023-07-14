import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from loguru import logger
list_promotion = ['x2_1', 'x5_1', 'x10_1', 'x15_1', 'x20_1', 'x2_7', 'x5_7', 'x10_7',
                  'x15_7', 'x20_8', 'highlight', 'xl']


def get_method_promotions(driver, data):
    try:
        item = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
        for announcement in item:
            try:
                point = announcement.find_element(By.CLASS_NAME, 'styles-arrow-jfRdd')
                ActionChains(driver).move_to_element(point).perform()
                time.sleep(5)
                images = driver.find_elements(By.CLASS_NAME, 'style-image-wPviB')
                method_promotions = []
                for image in images:
                    image_property = image.get_property('src')
                    for prom in list_promotion:
                        if prom in image_property:
                            method_promotions.append(prom)

                data.method_promotions = ', '.join(method_promotions)
            except Exception as ex:
                data.method_promotions = ''

    except Exception as ex:
        logger.error(f'Ошибка в методах продвижения {ex}')

if __name__ == "__main__":
    pass