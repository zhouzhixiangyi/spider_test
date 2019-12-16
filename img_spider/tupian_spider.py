import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import time
import re


if __name__ == '__main__':
    list_url = []
    for i in range(1,3):
        if i == 1:
            url = 'http://www.shuaia.net/meinv/index.html'
        else:
            url = 'http://www.shuaia.net/meinv/index_%d.html'%i

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        res = requests.get(url , headers = headers)
        res.encoding='utf-8'
        html = res.text
        bf = BeautifulSoup(html , 'lxml')
        targets_url = bf.find_all(class_='item-img')
        for each in targets_url:
            list_url.append(each.img.get('alt') + '=' + each.get('href'))

    print('连接采集完成')

    for each in list_url:
        img_info = each.split('=')
        target = img_info[1]
        filename = img_info[0] + '.jpg'
        print('下载:'+filename)
        headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        img_res = requests.get(target,headers=headers)
        img_res.encoding='utf-8'
        img_html = img_res.text
        img_bf_1 = BeautifulSoup(img_html,'lxml')
        img_url = img_bf_1.find_all('div' ,class_='wr-single-content-list')
        img_bf_2 = BeautifulSoup(str(img_url), 'lxml')

        img_url = img_bf_2.div.img.get('src')
        if re.match(r'^/',img_url):
            img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
        if 'images' not in os.listdir():
            os.makedirs('images')
        urlretrieve(url=img_url, filename='images/' + filename)
        time.sleep(1)
    print('下载完成！')
















# if __name__ == '__main__':
#     target_url = 'http://www.shuaia.net/rihanshuaige/2017-05-18/1294.html'
#     filename = '张根硕拍摄机车型男写真帅气十足' + '.jpg'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#     }
#     img_res = requests.get(target_url , headers=headers)
#     img_res.encoding='utf-8'
#     img_html = img_res.text
#     img_bf_1 = BeautifulSoup(img_html,'lxml')
#     img_url = img_bf_1.find_all('div',class_='wr-single-content-list')
#     img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
#     img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
#     if 'images' not in os.listdir():
#         os.makedirs('images')
#     urlretrieve(url=img_url, filename='images/' + filename)
#     print('下载完成！')
#













# if __name__ == '__main__':
#     list_utl = []
#     for i in range(1,20):
#         if i == 1:
#             url = 'http://www.shuaia.net/meinv/index.html'
#         else:
#             url = 'http://www.shuaia.net/meinv/index_%d.html'%i
#
#         ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
#         headers = {
#             'user-agent':ua
#         }
#         res = requests.get(url , headers = headers)
#         res.encoding = 'utf-8'
#         html = res.text
#
#         bf = BeautifulSoup(html , 'lxml')
#         target_url = bf.find_all(class_='item-img')
#
#         for each in target_url:
#             list_utl.append(each.img.get('alt') + '=' + each.get('href'))
#     print(list_utl)






























# if __name__ == '__main__':
#     url = "http://www.shuaia.net/e/tags/?tagname=%E7%BE%8E%E5%A5%B3"
#     ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
#     head = {'user-agent':ua}
#     req = requests.get(url , headers=head)
#     req.encoding = 'utf-8'
#     html = req.text
#     # print(html)
#     bf = BeautifulSoup(html , 'lxml')
#     targets_url = bf.find_all(class_='item-img')
#     # print(targets_url)
#     list_url = []
#     for each in targets_url:
#         list_url.append(each.img.get('alt')+'='+each.get('href'))
#     print(list_url)