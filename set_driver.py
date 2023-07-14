from selenium.webdriver.chrome.service import Service # нужно для того чтобы передавать путь до драйвера
from fake_useragent import UserAgent
from selenium import webdriver


ua = UserAgent().chrome
options = webdriver.ChromeOptions()

path_driver = Service(executable_path='chromedriver_mac64/chromedriver')

options.add_argument('Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
options.add_argument('Accept-Encoding = gzip, deflate')
options.add_argument('Accept-Language = ru')
options.add_argument('Cache-Control = max-age=0')
options.add_argument('Host = www.httpbin.org')
options.add_argument('Upgrade-Insecure-Requests = 1')
options.add_argument('User-Agent= Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML,'
                     'like Gecko) Version/16.3 Safari/605.1.15')
options.add_argument('X-Amzn-Trace-Id = Root=1-64a296ac-0604efda58e43c945b2341c6')
options.add_argument('--disable-blink-features=AutomationControlled') # аргумент чтобы сайт не видел веб драйвер

driver = webdriver.Chrome(service=path_driver, options=options)


if __name__ == "__main__":
    pass
