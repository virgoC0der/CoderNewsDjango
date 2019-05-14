import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate import dataModel

head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'github.com',
            'Referer': 'https://github.com/explore',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

def github():
    trendingUrl = "https://github.com/trending/"
    categoryArray = ["python", "c++", "c", "swift", "java", "javascript"]
    for category in categoryArray:
        url = trendingUrl + category + "?since=daily"
        res = requests.get(url, headers=head)
        soup = BeautifulSoup(res.text, "html.parser")
        projectList = soup.findAll("li", class_="col-12 d-block width-full py-4 border-bottom")
        for project in projectList:
            title = project.find('h3').find('a').get("href")[1:]
            project_url = "https://github.com/" + title
            try:
                describe = project.find('p', class_="col-9 d-inline-block text-gray m-0 pr-4").get_text().rstrip().lstrip() + " " + title
            except:
                describe = title
            model = dataModel.dataModel(describe, project_url, "", category)
            model.printIt()
            try:
                model.updateToInfo()
            except:
                continue

# 获取explore页面文章
def get_article():
    url = "https://github.com/explore"
    res = requests.get(url, headers=head)
    soup = BeautifulSoup(res.text, "html.parser")
    article_list = soup.find("div", class_="d-lg-flex gutter-lg-condensed").find_all("article")
    for article in article_list:
        article_url = article.find("a").get("href")
        img_url = article.find("img").get("src")
        title = article.find("h1").get_text()
        model = dataModel.dataModel(title.lstrip(), article_url.lstrip(), img_url, "github")
        model.printIt()
        try:
            model.updateToInfo()
        except:
            continue