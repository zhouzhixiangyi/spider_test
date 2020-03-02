import re
import requests
key = "Java"
hd = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
res = requests.get("https://search.51job.com/list/000000,000000,0000,00,9,99,"+key+",2,1.html", headers=hd)
data = bytes(res.text, res.encoding).decode("gbk", 'ignore')
pat_page = "共(.*?)条职位"
allline = re.compile(pat_page, re.S).findall(data)[0]
allpage = int(allline)//50 + 1
for i in range(0, allpage):
    print("---正在爬"+str(i+1)+"页---")
    res = requests.get("https://search.51job.com/list/000000,000000,0000,00,9,99,"+key+",2,"+str(i+1)+".html", headers=hd)
    thisdata = bytes(res.text, res.encoding).decode("gbk", 'ignore')
    # print(thisdata)
    job_url_pat = '<p class="t1 ">.*?href="https://jobs.51job.com/(.*?).html?'
    job_url_all = re.compile(job_url_pat, re.S).findall(thisdata)[1:]
    print(job_url_all)
    for job_url in job_url_all:
        this_url = "https://jobs.51job.com/"+job_url+".html"
        res = requests.get(this_url)
        thisdata = bytes(res.text, res.encoding).decode("gbk", 'ignore')
        pat_title = '<h1 title="(.*?)"'
        pat_company = 'p class="cname">.*?title="(.*?)"'
        pat_money = '<div class="cn">.*?<strong>(.*?)</strong>'
        pat_msg = '<div class="bmsg job_msg inbox">(.*?)<div class="share">'
        title = re.compile(pat_title, re.S).findall(thisdata)[0]
        company = re.compile(pat_company, re.S).findall(thisdata)[0]
        money = re.compile(pat_money, re.S).findall(thisdata)[0]
        msg = re.compile(pat_msg, re.S).findall(thisdata)[0]
        print('-----')
        print(title)
        print(company)
        print(money)
