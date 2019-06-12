import re
import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *

def getZol():
    dataArray = []
    url = "http://safe.zol.com.cn/more/2_1628.shtml"
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    div_set = soup.find_all("div", class_="info-mod clearfix")
    for div in div_set:
        title = div.find("a").find("img").get("alt")
        eachUrl = div.find("a").get("href")
        if(div.find("a").find("img").get(".src") != None):
            imageUrl = div.find("a").find("img").get(".src")
        else:
            imageUrl = div.find("a").find("img").get("src")
        model = dataModel(title, eachUrl, imageUrl, 'NetworkSecurity')
        try:
            model.updateToInfo()
            model.printIt()
        except:
            continue