import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *


head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'github.com',
            'Referer': 'https://github.com/explore',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

def getGithubTrending():
    url = "https://github.com/trending/swift?since=daily"
    res = requests.get(url, headers=head)
    soup = BeautifulSoup(res.text, "html.parser")
    projectList = soup.findAll("li", class_="col-12 d-block width-full py-4 border-bottom")
    for project in projectList:
        title = project.find('h3').find('a').get("href")[1:]
        project_url = "https://github.com/" + title
        try:
            describe = project.find('p', class_="col-9 d-inline-block text-gray m-0 pr-4").get_text().rstrip().lstrip() + " " + title
        except:
            describe = title
        model = dataModel(describe, project_url, None, "swift")
        model.printIt()
        model.updateToInfo()

if __name__ == "__main__":
    array = getGithubTrending()
    for item in array:
        item.printIt()