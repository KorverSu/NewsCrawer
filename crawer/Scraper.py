import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

DRIVER_PATH = "./driver/chromedriver"


class Scraper:
    def __init__(self):
        self.__driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.__page = 1

    def close_driver(self):
        self.__driver.close()

    def visit_tvbs(self, news_id: str):
        url = "https://news.tvbs.com.tw/politics/{}".format(news_id)
        self.__driver.get(url)
        try:
            title_box = self.__driver.find_element(By.CLASS_NAME, "title_box")
            title = title_box.find_element(By.CLASS_NAME, "title").text
            author = self.__driver.find_element(By.CLASS_NAME, "author")
            contents = self.__driver.find_element(By.CLASS_NAME, "article_content").text
            time_list = author.text.split("\n")
            release_time = time_list[1].strip("發佈時間：")
            last_updated = time_list[2].strip("最後更新時間：")
            print(title)
            print(release_time)
            print(last_updated)
            print(contents)
        except Exception as e:
            print("The tvbs url is invalid: ", e)

    def visit_setn(self, news_id: str):
        # 三立新聞
        url = "https://www.setn.com/News.aspx?NewsID={}".format(news_id)
        self.__driver.get(url)
        try:
            title = self.__driver.find_element(By.CLASS_NAME, "news-title-3").text
            release_time = self.__driver.find_element(By.CLASS_NAME, "page-date").text
            contents = self.__driver.find_element(By.TAG_NAME, "article").text
            print(title)
            print(release_time)
            print(contents)
        except Exception as e:
            print("The setn url is invalid: ", e)

    def visit_ebc(self):
        # 東森
        url = "https://news.ebc.net.tw/news/politics"
        self.__driver.get(url)
        while 1:
            try:
                news_list = self.__driver.find_elements(By.CLASS_NAME, "style1")
                news_list = [x for x in news_list if "white-box" in x.get_attribute("class")]
                for news in news_list:
                    tmp_driver = webdriver.Chrome(executable_path=DRIVER_PATH)
                    release_time = news.find_element(By.CLASS_NAME, "small-gray-text").text
                    ref = news.find_element(By.TAG_NAME, "a")
                    url = ref.get_attribute("href")
                    title = ref.get_attribute("title")
                    print(url)
                    print(title)
                    print(release_time)
                    tmp_driver.get(url)
                    page = tmp_driver.find_element(By.CLASS_NAME, "raw-style")
                    contents = page.find_element(By.TAG_NAME, "div").text
                    print(contents)
                    time.sleep(2)
                    tmp_driver.close()
                    # break  # for test
                butt = self.__driver.find_element(By.CLASS_NAME, "white-btn")
                self.__page += 1
                js = "arguments[0].setAttribute('data-page', '{}');".format(str(self.__page))
                self.__driver.execute_script(js, butt)
                butt.click()
                time.sleep(2)
            except Exception as e:
                print("The ebc url is invalid: ", e)


if __name__ == '__main__':
    sc = Scraper()
    # sc.visit_tvbs('2')
    # sc.visit_tvbs('80018')
    # sc.visit_setn('1272355')
    sc.visit_ebc()
    sc.close_driver()
