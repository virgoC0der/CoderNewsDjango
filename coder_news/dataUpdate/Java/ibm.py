from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import dataModel
import requests

def get_ibm():
    url = "https://developer.ibm.com/technologies/java/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    home = soup.find("a", class_="ibm--hub__block_link")
    home_title = home.find("h3", class_="ibm--hub__title").find("span").get_text()
    home_url = "https://developer.ibm.com" + home.get("href")
    model = dataModel(home_title, home_url, "", "java")
    try:
        model.updateToInfo()
    except:
        print("Duplicate!")
    print(home_title, home_url)
    article_list = soup.find_all("a", class_="ibm--card__block_link")
    for article in article_list:
        title = article.find("h3").get_text()
        article_url = "https://developer.ibm.com" + article.get("href")
        image_url = ""
        if article.find("img") != None:
            image_url = article.find("img").get("src")
        model = dataModel(title, article_url, image_url, "java")
        model.printIt()
        try:
            model.updateToInfo()
        except:
            continue
