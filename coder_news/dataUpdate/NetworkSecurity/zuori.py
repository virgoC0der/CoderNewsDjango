import urllib
import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *

def getZuori():
    dataArray = []
    url = "https://www.anquanke.com/"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    div_set = soup.find_all("div", class_="col col-9 col-xs-9 col-sm-8 col-md-8 col-lg-6 col-xl-6 common-item-left")
    for div in div_set:
        title = div.find_next_sibling().find("div").find("div").find("a").get_text()
        eachUrl = "https://www.anquanke.com" + div.find("a").get("href")
        imageUrl = div.find("a").find("div").find("div").find("img").get("data-original")
        model = dataModel(title, eachUrl, imageUrl, 'NetworkSecurity')
        try:
            model.updateToInfo()
            model.printIt()
        except:
            continue