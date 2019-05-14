from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import dataModel
import requests


def getjrebel():
    url = "https://jrebel.com/rebellabs/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    article_list = soup.find_all("div", class_="post")
    for article in article_list:
        title = article.find("h1").find("a").get("title")
        article_url = article.find("h1").find("a").get("href")
        try:
            image_url = "https://jrebel.com" + article.find("img").get("src")
            model = dataModel(title, article_url, image_url, "java")
            print(title, article_url, image_url, "img")
        except:
            model = dataModel(title, article_url, "", "java")
            print(title, article_url)
        try:
            model.updateToInfo()
        except:
            continue
