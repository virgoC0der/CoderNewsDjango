import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *



def getHackeingWithSwift():
    dataArray = []
    websiteUrl = "https://www.raywenderlich.com"
    url = "https://www.raywenderlich.com/library/search?section_id=49&domain_ids%5B%5D=1&content_types%5B%5D=article&category_ids%5B%5D=156&category_ids%5B%5D=159&category_ids%5B%5D=157&category_ids%5B%5D=151&category_ids%5B%5D=145&category_ids%5B%5D=161&category_ids%5B%5D=143&category_ids%5B%5D=147&category_ids%5B%5D=155&category_ids%5B%5D=144&category_ids%5B%5D=158&category_ids%5B%5D=148&category_ids%5B%5D=150&category_ids%5B%5D=152&category_ids%5B%5D=160&category_ids%5B%5D=149&category_ids%5B%5D=153&category_ids%5B%5D=154&category_ids%5B%5D=146&sort_order=released_at&page=1"
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    title_set = soup.find_all("span",class_="c-tutorial-item__title")
    print(soup.prettify())
    titleArray = []
    urlArray = []
    imageurlArray = []
    for title in title_set:
        titleArray.append(title.getText())
    a_set = soup.find_all("a")
    for a in a_set:
        urlArray.append(websiteUrl + a.get("href"))
    image_set = soup.find_all(class_="c-tutorial-item__art-image--primary")
    for image in image_set:
        imageurlArray.append(image.get("src"))
    for index in range(0,10):
        dataArray.append(dataModel(titleArray[index],urlArray[index],imageurlArray[index],"swift"))
        model = dataModel(titleArray[index],urlArray[index],imageurlArray[index],"swift")
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