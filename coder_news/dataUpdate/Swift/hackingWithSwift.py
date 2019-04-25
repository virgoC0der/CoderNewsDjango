import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *

def getHackeingWithSwift():
    dataArray = []
    url = "https://www.hackingwithswift.com/articles"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    div_set = soup.find_all("a")
    for div in div_set:
        h3 = div.find("h3")
        if h3 != None:
            title = h3.get_text()
            eachUrl = "https://www.hackingwithswift.com" + div.get("href")
            imageUrl = "https://www.hackingwithswift.com" + div.find("img").get("src")
            dataArray.append(dataModel(title,eachUrl,imageUrl,"swift"))
            model = dataModel(title, eachUrl, imageUrl, "swift")
            model.printIt()
            try:
                model.updateToInfo()
            except:
                continue
    return dataArray

if __name__ == "__main__":
    array = getHackeingWithSwift()
    for item in array:
        item.printIt()