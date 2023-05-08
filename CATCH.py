import time
import schedule
import requests
from bs4 import BeautifulSoup

from selenium import webdriver


driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://sys.leadyoung.com.tw/assets/Home/LINE_BOT_TEST?ID=WO240410001')
time.sleep(10)

""" search = driver.find_element('id', 'DivResult')
print(search.text) """

""" account = driver.find_element('id', 'txtAccount')
password = driver.find_element('id', 'txtPassword')
login = driver.find_element('id', 'btnConfirm')
account.send_keys('gogoandcindy')
password.send_keys('lye') 
login.click()
time.sleep(15)"""

""" search = driver.find_element('id', 'lbInStock_TF')
print(search.text) """


""" def catch():
    # 要抓取的網頁URL
    url = 'http://tycpaipai.leadyoung.com.tw/vLINE_BOT_TEST?ID=WO240410001'

    # 發送GET請求
    response = requests.get(url)

    # 解析HTML內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有的超連結
    links = soup.find_all(
        'div', class_="logo_under_text", limit=1)

    # 輸出每個超連結的文字和URL
    for link in links:
        print(link.text)


def job():
    print("I'm working...")


schedule.every(5).seconds.do(catch)

while True:
    schedule.run_pending()
    time.sleep(1) """
