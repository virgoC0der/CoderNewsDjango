import requests
from coder_news.dataUpdate.dataModel import *
def getSspai():
    url = "https://sspai.com/api/v1/articles?offset=0&limit=20&has_tag=1&tag=%E5%BA%94%E7%94%A8%E6%8E%A8%E8%8D%90&include_total=false&type=recommend_to_home"
    list = requests.get(url).json()
    dataArray = []
    llist = list['list']
    for i in range(len(llist)):
        title = llist[i]['title']
        eachUrl = "https://sspai.com/post/" + str(llist[i]['id'])
        imageUrl = "https://cdn.sspai.com/" + llist[i]['banner']
        model = dataModel(title, eachUrl, imageUrl, 'Technology')
        try:
            model.updateToInfo()
            model.printIt()
        except:
            continue