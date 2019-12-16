import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery as pq
from taobao_meishi.config import *

import pymongo
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# browser = webdriver.Chrome(options=chrome_options)

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)


def search():
    print('正在搜索')
    try:
        browser.get('https://www.taobao.com/')
        inputs =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        submit= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        inputs.send_keys(KEYWORDS)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    print('当前页数：',page_number)
    try:
        inputs = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pnum')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        inputs.clear()
        inputs.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        get_products()

    except TimeoutException:
        return next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        # save_to_mongo(product) # 存储到数据库


def save_to_mongo(result):
    try:

        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功！',result)
    except Exception:
        print('存储失败',result)


def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total+1):
        next_page(i)

if __name__ == '__main__':
    main()




