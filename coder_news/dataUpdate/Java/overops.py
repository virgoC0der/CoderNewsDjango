from bs4 import BeautifulSoup
import requests
from coder_news.dataUpdate.dataModel import dataModel

head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://blog.overops.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

def get_overops():
    url = "https://blog.overops.com/"
    res = requests.get(url, headers=head)
    soup = BeautifulSoup(res.text, "html.parser")
    article_list = soup.find_all("article")
    for article in article_list:
        title = article.find("div", class_="col-md-7 col-sm-7 right-post-content").find("h2").find("a").get_text()
        article_url = article.find("div", class_="col-md-7 col-sm-7 right-post-content").find("h2").find("a").get("href")
        img_url = article.find("div", class_="col-md-5 col-sm-5 post-featured-image").find("a").get("href")
        print(title, article_url, img_url)
        model = dataModel(title, article_url, img_url, "java")
        try:
            model.updateToInfo()
        except:
            continue