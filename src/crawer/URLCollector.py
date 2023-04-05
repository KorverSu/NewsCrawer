from selenium import webdriver
from src.config import DRIVER_PATH


class URLCollector:
    def __init__(self):
        self.__driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.__tvbs_num = 2000000  # tvbs新聞數量大概有 2000000
        self.__setn_num = 1300000  # tvbs新聞數量大概有 三立

    def close_driver(self):
        self.__driver.close()

    def get_tvbs_url(self):
        for news_id in range(self.__tvbs_num):
            url = "https://news.tvbs.com.tw/politics/{}".format(news_id)