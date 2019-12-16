import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import time


if __name__ == '__main__':
    list_url = []
    for i in range(1,20):
        if i == 1:
            url = 'http://pic.netbian.com/4kmeinv/'
        else:
            url = 'http://pic.netbian.com/4kmeinv/index_%d.html'%i

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        res = requests.get(url , headers = headers)
        res.encoding='gbk'
        html = res.text
        # print(html)
        bf = BeautifulSoup(html , 'lxml')
        targets_url = bf.find_all(attrs={"target":"_blank"})[1:-8]
        # print(targets_url)
        for each in targets_url:

            list_url.append(each.b.string + '=http://pic.netbian.com' + each.get('href'))

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
        img_res.encoding='gbk'
        img_html = img_res.text
        img_bf = BeautifulSoup(img_html,'lxml')
        img_url = img_bf.find_all(attrs={"id":"img"})
        # print(img_url)
        img_url = 'http://pic.netbian.com' + img_bf.img.get('src')
        if 'images' not in os.listdir():
            os.makedirs('images')
        urlretrieve(url=img_url, filename='images/' + filename)
        time.sleep(1)
    print('下载完成！')



