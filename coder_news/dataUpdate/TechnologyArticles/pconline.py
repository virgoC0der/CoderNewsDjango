import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *

def getPconline():
    dataArray = []
    url = "https://mobile.pconline.com.cn/pry/"
    result = requests.get(url)
    result.encoding = "gbk"
    soup = BeautifulSoup(result.text, "html.parser")
    div_set = soup.find("div", class_="art-list art-list-cut").find_all("a", class_="img-area")
    for div in div_set:
        title = div.find("img").get("alt")
        eachUrl = div.get("href")
        imageUrl = "https://" + div.find("img").get("src")
        model = dataModel(title, eachUrl, imageUrl, 'Technology')
        try:
            model.updateToInfo()
            model.printIt()
        except:
            continue