from django.utils.timezone import now, timedelta
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

from coder_news import models

head_v2ex = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'www.v2ex.com',
        'Referer': 'http://www.v2ex.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    }

head_github = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'github.com',
            'Referer': 'https://github.com/explore',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

def crawler_v2ex(request):
    categoryArray = ["java","python"]
    imageUrl = None
    for category in categoryArray:
        url = "https://www.v2ex.com/go/" + category
        res = requests.get(url, headers=head_v2ex)
        soup = BeautifulSoup(res.text, "html.parser")
        tagList = soup.findAll("span", class_="item_title")
        # id = int(str(models.Info.objects.all()[:1].values("id"))[18:-3])
        for tag in tagList:
            title = tag.get_text()
            href = "https://www.v2ex.com" + tag.find('a').get("href")
            try:
                id = updateToInfo(title, href, imageUrl, category+",v2ex")
                updateToChild(category, id)
            except:
                print("Duplicate error!")
    return HttpResponse("添加成功！")

def crawler_github(request):
    trending_url = "https://github.com/trending"
    categoryArray = ["python", "swift", "java"]
    imageUrl = None
    for category in categoryArray:
        url = trending_url + "/" + category + "?since=daily"
        print(url)
        res = requests.get(url, headers=head_github)
        soup = BeautifulSoup(res.text, "html.parser")
        list = soup.findAll("li", class_="col-12 d-block width-full py-4 border-bottom")
        for l in list:
            title = l.find('h3').find('a').get("href")[1:]
            print(title)
            project_url = "https://github.com/" + title
            try:
                describe = l.find('p', class_="col-9 d-inline-block text-gray m-0 pr-4").get_text()
                describe = describe.rstrip().lstrip()
                print(describe)
                id = updateToInfo(title + " " + describe, project_url, imageUrl, category+",github")  # 更新主表并获取id
            except:
                print("no describe")
                id = updateToInfo(title, project_url, imageUrl, category+",github")       # 更新主表并获取id
            updateToChild(category, id)                                     # 更新子表
            updateToChild("github", id)

# 添加到子表
def updateToChild(category, id):
    date = now().date() + timedelta(days=0)
    if category == "python":
        models.python.objects.create(create_time=date, infoId_id=id)
    if category == "java":
        models.Java.objects.create(create_time=date, infoId_id=id)
    if category == "swift":
        models.swift.objects.create(create_time=date, infoId_id=id)
    if category == "github":
        models.github.objects.create(create_time=date, infoId_id=id)


# 添加到主表
def updateToInfo(title,url,imageUrl, category):
    time = now().date() + timedelta(days=0)
    models.Info.objects.create(title=title, url=url, imageURL=imageUrl, category=category, create_time=time)
    id = int(str(models.Info.objects.latest("id"))[13:-1])
    return id