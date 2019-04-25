import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *

def getNshipster():
    dataArray = []
    url = "https://nshipster.com"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    div_set = soup.find_all("a",class_="title")
    titleArray = []
    urlArray = []
    for div in div_set:
        title = div.get_text()
        theURL = url + div.get("href")
        urlArray.append(theURL)
        # eachUrl = "https://www.hackingwithswift.com" + div.get("href")
        # imageUrl = "https://www.hackingwithswift.com" + div.find("img").get("src")
        # dataArray.append(dataModel(title,eachUrl,imageUrl,"swift"))
        titleArray.append(title)
    li_set = soup.find_all("li")
    textArray = []
    for li in li_set:
        p = li.find("p")
        if p != None :
            text = p.getText()
            textArray.append(text)

    # print(titleArray)
    # print(urlArray)
    # print(textArray)
    for index in range(0,len(titleArray)):
        dataArray.append(dataModel(titleArray[index]+textArray[index],urlArray[index],None,"swift"))
    return dataArray

if __name__ == "__main__":
    array = getNshipster()
    for item in array:
        item.printIt()