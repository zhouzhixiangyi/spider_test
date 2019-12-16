from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from multiprocessing import Pool
from s_2taobao.mysql_2taobao import ConnMysql

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)  # options=chrome_options
wait = WebDriverWait(driver, 20)
driver.get('https://2.taobao.com/')
mysql = ConnMysql()
# 分类名
category = []
doc1 = pq(driver.page_source)
items1 = doc1('body > div.main > div.tabbar-wrap .item').items()
for item1 in items1:
    category.append(item1.text())
# print(category)


def get_all_page(number):
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main > div.tabbar-wrap > div:nth-child({}) > p'.format(str(number)))))
    driver.execute_script("arguments[0].click();", submit)
    return category[number-1]


def get_page_url(number, c):
    try:
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'body > div.main > div.pagination > div > ul > li.number.active'), str(number)))
        html = driver.page_source
        doc = pq(html)
        items = doc('body > div.main > div.item-list > div > a').items()
        for item in items:
            head = item.attr('href')
            url = 'https:' + head
            get_product(url, c)
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.main > div.pagination > div > button.btn-next')))
        # submit.click()
        driver.execute_script("arguments[0].click();", submit)
    except TimeoutException:
        return get_page_url(number)


def get_product(url, c):
    try:
        p_driver = webdriver.Chrome(options=chrome_options)
        p_driver.get(url)
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#idle-detail > div.layout.grid-s730m0')))
        doc = pq(p_driver.page_source)
        # 时间
        time = doc('#idle-detail > div.top-nav.clearfix > div.others-wrap > ul > li:nth-child(2) > span').text()
        # 标题
        title = doc('#J_Property > h1').text()
        # 价格
        price = doc('#J_Property > ul.price-info > li > span.price.big > em').text()
        # 成色
        quality = doc('#J_Property > ul.idle-info > li:nth-child(1) > em').text()
        # 地址
        address = doc('#J_Property > ul.idle-info > li:nth-child(2) > em').text()

        all_img = []
        img_list = doc('#J_Slider > ul > li > a > .big-img').items()
        for i in img_list:
            if i.attr('src') != '//assets.alicdn.com/p/fp/2011a/assets/space.gif':
                all_img.append('https:' + i.attr('src'))
        # 介绍
        introduction = doc('#J_DescContent').text()
        product = {
            'category': c,
            'time': time,
            'title': title,
            'price': price,
            'quality': quality,
            'address': address,
            'img_list': all_img,
            'introduction': introduction,
        }
        print(product)
        # 保存到mysql中
        mysql.insert(product)

    except TimeoutException:
        return get_product(url)
    finally:
        p_driver.close()


def main():
    for j in range(1, 9):
        c = get_all_page(j)
        for i in range(1, 11):
            get_page_url(i, c)
    driver.close()


if __name__ == '__main__':
    main()
    # get_page_url(1)
    # for i in range(1, 11):
    #     get_page_url(i)
    # driver.close()




















