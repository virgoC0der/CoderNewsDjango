from django.http import HttpResponse

from coder_news.dataUpdate import github
from coder_news.dataUpdate.Java import ibm, importnew, javaworld, jrebel, overops
from coder_news.dataUpdate.Swift import appcoda, githubTrendingSwift, hackingWithSwift, nshipster, raywenderlich, swift_org
from coder_news.dataUpdate.NetworkSecurity import zol, zuori
from coder_news.dataUpdate.TechnologyArticles import appso, igao7, pcbeta, pcbetaTech, pconline, souhu, souhuArticles, sspaiArticles, sspaiSharingArticles

def update(request):
    appcoda.getAppcoda()
    githubTrendingSwift.getGithubTrending()
    hackingWithSwift.getHackeingWithSwift()
    nshipster.getNshipster()
    raywenderlich.getHackeingWithSwift()
    swift_org.getSwiftOrg()
    github.get_article()
    ibm.get_ibm()
    # importnew.get_import_new()
    javaworld.get_java_world()
    jrebel.getjrebel()
    overops.get_overops()
    zol.getZol()
    zuori.getZuori()
    appso.getAppso()
    igao7.getIgao7()
    pcbeta.getPcbeta()
    pcbetaTech.getPcbeta_tech()
    pconline.getPconline()
    souhu.getSouhu()
    souhuArticles.getSouhuArticles()
    sspaiArticles.getSspai()
    sspaiSharingArticles.getSspai()
    return HttpResponse("Done!")

