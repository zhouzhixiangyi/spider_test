import requests
from requests.exceptions import RequestException
import re
import json

url = 'https://careers.tencent.com/tencentcareer/api/post/Query?countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={index}&pageSize=10&language=zh-cn&area=cn'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
headers = {
    'user-agent': ua,
}
res = requests.get(url.format(index=1), headers=headers)
results = json.loads(res.text)
if 'Data' in results.keys():
    count = results.get('Data').get('Count')
for i in range(1, count+1):
    res = requests.get(url.format(index=i), headers=headers)
    results = json.loads(res.text)
    items = results.get('Data').get('Posts')
    if items:
        for item in items:
            data = {
                'RecruitPostName' : item.get('RecruitPostName'),
                'CountryName' : item.get('CountryName'),
                'LocationName' : item.get('LocationName'),
                'BGName' : item.get('BGName'),
                'CategoryName' : item.get('CategoryName'),
                'Responsibility' : item.get('Responsibility'),
                'LastUpdateTime' : item.get('LastUpdateTime'),
                'PostURL': item.get('PostURL'),
            }
            with open('岗位信息.json', 'a', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False)
                outfile.write('\n')









