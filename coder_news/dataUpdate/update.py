from django.http import HttpResponse

from coder_news.dataUpdate import github
from coder_news.dataUpdate.Java import ibm, importnew, javaworld, jrebel, overops
from coder_news.dataUpdate.Swift import appcoda, githubTrendingSwift, hackingWithSwift, nshipster, raywenderlich, swift_org
from coder_news.dataUpdate.Python import github_trending
import time

def update():
    github_trending.getPythonGithubTrending()
    githubTrendingSwift.getGithubTrending()
    appcoda.getAppcoda()
    time.sleep(3)
    hackingWithSwift.getHackeingWithSwift()
    nshipster.getNshipster()
    raywenderlich.getHackeingWithSwift()
    swift_org.getSwiftOrg()
    time.sleep(3)
    # github.get_article()
    # importnew.get_import_new()
    javaworld.get_java_world()
    jrebel.getjrebel()
    overops.get_overops()
    ibm.get_ibm()
    # return HttpResponse("Done!")

