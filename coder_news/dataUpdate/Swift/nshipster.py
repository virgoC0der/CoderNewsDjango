import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *

def getNshipster():
    url = "https://nshipster.com"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    # div_set = soup.find_all("a",class_="title")
    li_set = soup.find("section", id="recent").find_all("li")
    for li in li_set:
        title = li.find("a").get_text()
        text = li.find("p").get_text()
        eachUrl = url + li.find("a").get("href")
        model = dataModel(title, eachUrl, None, "swift")
        model.printIt()
        try:
            model.updateToInfo()
        except:
            continue