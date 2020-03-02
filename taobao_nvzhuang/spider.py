import urllib.request
import re
import random
from spider_test.taobao_nvzhuang.config import ua_pools

keyname = '女装'
key = urllib.request.quote(keyname)


def ua(ua_pools):
    this_ua = random.choice(ua_pools)
    print(this_ua)
    headers = ("User-agent", this_ua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)


for i in range(0, 100):
    print("----第"+str(i)+"页商品----")
    url = "https://re.taobao.com/search?keyword="+key+"&page="+str(i)
    ua(ua_pools)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")

    pat = '<div class="item">.*?href="(.*?)"'
    pat_title = '<span class="title" title="(.*?)"'
    pat_price = '<span class="pricedetail">.*?<strong>(.*?)</strong>'
    pat_payNum = '<span class="payNum">(.*?)</span>'
    pat_score = '<span class="active dsr-info-tgr".*?"dsr-info-num">(.*?)</span>'

    url_list = re.compile(pat, re.S).findall(data)
    title = re.compile(pat_title, re.S).findall(data)
    price = re.compile(pat_price, re.S).findall(data)
    pay_num = re.compile(pat_payNum, re.S).findall(data)
    score = re.compile(pat_score, re.S).findall(data)
    for j in range(0, len(title)):
        print(title[j], price[j], pay_num[j], score[j])









