from django.utils.timezone import now, timedelta
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

from coder_news import models

head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.v2ex.com',
        'Referer': 'http://www.v2ex.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    }

def updateToInfo():
    category = "java"
    url = "https://www.v2ex.com/go/" + category
    res = requests.get(url, headers=head)
    soup = BeautifulSoup(res.text, "html.parser")
    tagList = soup.findAll("span", class_="item_title")
    # id = int(str(models.Info.objects.all()[:1].values("id"))[18:-3])
    for tag in tagList:
        date = now().date() + timedelta(days=0)
        title = tag.get_text()
        href = "https://www.v2ex.com" + tag.find('a').get("href")
        try:
            models.Info.objects.create(title=title, url=href, create_time=date, category=category+",v2ex")
            pass
        except:
            print("Duplicate error!")
            # id -= 1
        id = int(str(models.Info.objects.latest("id"))[13:-1])
        updateToChild(category, id, date)
    print("添加成功！")


def updateToChild(category, id, date):
    if category == "python":
        models.python.objects.create(create_time=date, infoId_id=id)
    if category == "java":
        models.Java.objects.create(create_time=date, infoId_id=id)


