import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *
def getGithubTrending():
    dataArray = []
    url = "https://github.com/trending/swift?since=daily"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    div_set = soup.find_all("div",class_="d-inline-block col-9 mb-1")
    for div in div_set:
        title = div.find("h3").find("a").get_text()
        eachUrl = "https://github.com" + div.find("h3").find("a").get("href")
        # imageUrl = "https://www.hackingwithswift.com" + div.find("img").get("src")
        imageUrl = None
        print(title)
        print(eachUrl)
        dataArray.append(dataModel(title,eachUrl,imageUrl,"swift"))
    return dataArray

if __name__ == "__main__":
    array = getGithubTrending()
    for item in array:
        item.printIt()