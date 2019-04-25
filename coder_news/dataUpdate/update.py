from django.utils.timezone import now, timedelta
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

from coder_news import models
from coder_news.dataUpdate import github
from coder_news.dataUpdate.Swift import appcoda, githubTrendingSwift, hackingWithSwift, nshipster, raywenderlich, swift_org

def update():
    appcoda.getAppcoda()
    githubTrendingSwift.getGithubTrending()
    hackingWithSwift.getHackeingWithSwift()
    nshipster.getNshipster()
    raywenderlich.getHackeingWithSwift()
    swift_org.getSwiftOrg()
    return HttpResponse("Done!")

