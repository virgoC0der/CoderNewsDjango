import requests
import re
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *


def getSouhuArticles():
    dataArray = []
    imageUrlArray = []
    i = 0
    url = "http://it.sohu.com/882?spm=smpc.ch30.fd-ctag.24.1556018818504jdhz"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    div_set = soup.find_all(attrs={"data-role":"news-item"})
    for img in div_set:
        txt = str(img['class'])
        # 正则表达式
        p1 = r'txt'
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(p1)
        if(pattern.findall(txt)):
            noImg = None
            imageUrlArray.append(noImg)
        else:
            otherImg = "https://" + img.find("img").get("src")
            imageUrlArray.append(otherImg)
        title = img.find("h4").find("a").get_text().strip()
        eachUrl = "https:"+img.find("h4").find("a").get("href")
        model = dataModel(title, eachUrl, imageUrlArray[i], 'Technology')
        try:
            model.updateToInfo()
            model.printIt()
        except:
            continue
        i += 1