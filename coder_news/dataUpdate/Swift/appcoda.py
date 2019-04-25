import requests
from bs4 import BeautifulSoup
import re
from coder_news.dataUpdate.dataModel import *

def getAppcoda():
    dataArray = []
    imageArr = []
    i = 0
    url = "https://www.appcoda.com/tutorials/ios/"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    div_set = soup.find_all("div",class_="post-thumbnail")
    for div in div_set:
        txt = div.find("div").get("style")
        # 正则表达式
        p1 = r'https://.*g'
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(p1)
        imageUrl = str(pattern.findall(txt))
        # print(type(imageUrl))
        imageArr.append(str(imageUrl))
    div_set2 = soup.find_all("div",class_="post-content")
    for div in div_set2:
        title = div.find("h2").get_text()
        eachUrl = div.find("h2").find("a").get("href")
        dataArray.append(dataModel(title, eachUrl, imageArr[i], "swift"))
        model = dataModel(title, eachUrl, imageArr[i], "swift")
        model.printIt()
        i += 1
        try:
            model.updateToInfo()
        except:
            continue
    return dataArray

if __name__ == "__main__":
    array = getAppcoda()
    for item in array:
        item.printIt()