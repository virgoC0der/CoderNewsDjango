from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import dataModel
import requests

def get_import_new():
    url = "http://www.importnew.com/all-posts"
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        article_list = soup.find_all("div", class_="post-thumb")
        for article in article_list:
            a = article.find("a")
            title = a.get("title")
            article_url = a.get("href")
            image_url = a.find("img").get("src")
            model = dataModel(title, article_url, image_url, "java")
            try:
                model.updateToInfo()
            except:
                continue
    except:
        print("connection error")

