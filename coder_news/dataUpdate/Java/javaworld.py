from bs4 import BeautifulSoup
import requests
from coder_news.dataUpdate.dataModel import dataModel

def get_java_world():
    url = "https://www.javaworld.com"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    home_article = soup.find("div", class_="home-feature")
    home_title = home_article.find("div", class_="post-cont").find("a").get_text()
    home_url = url + home_article.find("div", class_="post-cont").find("a").get("href")
    home_image_url = home_article.find("figure", class_="feature-img").find("a").find("img").get("data-original")
    model = dataModel(home_title, home_url, home_image_url, "java")
    try:
        model.updateToInfo()
    except:
        print("Duplicate!")
    article_list = soup.find_all("div", class_="river-well article")
    for article in article_list:
        a = article.find("div", class_="post-cont").find("a")
        title = a.get_text()
        article_url = url + a.get("href")
        image_url = article.find("figure", class_="well-img").find("a").find("img").get("data-original")
        model = dataModel(title, article_url, image_url, "java")
        try:
            model.updateToInfo()
        except:
            continue

