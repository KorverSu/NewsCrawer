import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "driver/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://news.tvbs.com.tw/politics")
'''
box = driver.find_elements(By.CLASS_NAME, "txt_box")

for b in box:
    try:
        t = b.find_element(By.CLASS_NAME, "txt")
        ti = b.find_element(By.CLASS_NAME, "time")
        print(t.text)
        print(ti.text)
    except Exception:
        continue
'''
wait = WebDriverWait(driver, 10)

# 設定條件：等待class為'new-element'的元素出現
condition = EC.presence_of_element_located((By.CLASS_NAME, 'txt'))

# 持續等待新元素的出現
while True:
    try:
        # 等待新元素的出現
        new_element = wait.until(condition)

        # 獲得新元素的內容
        print(new_element.text)

    except:
        # 如果沒有新元素，跳出while迴圈
        break

# 關閉瀏覽器
driver.quit()


# link = driver.find_elements(By.LINK_TEXT, "‹ 上頁")

driver.close()
