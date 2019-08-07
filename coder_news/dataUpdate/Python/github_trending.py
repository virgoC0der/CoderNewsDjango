import requests
from bs4 import BeautifulSoup
from coder_news.dataUpdate.dataModel import *


def getPythonGithubTrending():
    url = "https://github.com/trending/python?since=daily"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    projectList = soup.findAll("article", class_="Box-row")
    for project in projectList:
        title = project.find('h1').find('a').get("href")[1:]
        project_url = "https://github.com/" + title
        try:
            describe = project.find('p', class_="col-9 text-gray my-1 pr-4").get_text().rstrip().lstrip() + " " + title
        except:
            describe = title
        model = dataModel(describe, project_url, "", "python")
        model.printIt()
        try:
            model.updateToInfo()
        except:
            continue