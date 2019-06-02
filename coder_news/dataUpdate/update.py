from django.http import HttpResponse

from coder_news.dataUpdate import github
from coder_news.dataUpdate.Java import ibm, importnew, javaworld, jrebel, overops
from coder_news.dataUpdate.Swift import appcoda, githubTrendingSwift, hackingWithSwift, nshipster, raywenderlich, swift_org

def update():
    appcoda.getAppcoda()
    githubTrendingSwift.getGithubTrending()
    hackingWithSwift.getHackeingWithSwift()
    nshipster.getNshipster()
    raywenderlich.getHackeingWithSwift()
    swift_org.getSwiftOrg()
    github.get_article()
    ibm.get_ibm()
    importnew.get_import_new()
    javaworld.get_java_world()
    jrebel.getjrebel()
    overops.get_overops()
    return HttpResponse("Done!")

