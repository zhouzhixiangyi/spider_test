from urllib.parse import urlencode

from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests
import json
import lxml
import re

def get_page_index(offset,keyword):

    data = {
        'aid': '24',
        'app_name': 'toutiao-web',
        'group_id': '6765085777224270339',
        'item_id': '6765085777224270339',
        'offset': '0',
        'count': '5'
    }
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    url = 'https://www.toutiao.com/api/pc/article/v4/tab_comments/?' + urlencode(data)

    try:
        response = requests.get(url,headers={'user-agent':ua})
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    print(data)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):

    try:
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        response = requests.get(url,headers={'user-agent':ua})
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错',url)
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html , 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    image_pattern = re.compile('gallery:.*?JSON.parse("(.*?))')

def main():
    html = get_page_index(0,'街拍')
    print(html)
    # for url in parse_page_index(html):
    #     html = get_page_detail(url)

if __name__ == '__main__':
    main()







