from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

DRIVER_PATH = "./driver/chromedriver"


class Scraper:
    def __init__(self):
        self.__driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def visit_tvbs(self, news_num: str):
        url = "https://news.tvbs.com.tw/politics/{}".format(news_num)
        self.__driver.get(url)
        try:
            author = self.__driver.find_element(By.CLASS_NAME, "author")
            content = self.__driver.find_elements(By.CLASS_NAME, "article_content")
            time_list = author.text.split("\n")
            release_time = time_list[1].strip("發佈時間：")
            last_updated = time_list[2].strip("最後更新時間：")
            print(release_time)
            print(last_updated)
            for c in content:
                print(c.text)
        except Exception as e:
            print("The url is invalid: ", e)


if __name__ == '__main__':
    sc = Scraper()
    sc.visit_tvbs('2')
    sc.visit_tvbs('80018')
    # sc.visit_tvbs('2080185')
