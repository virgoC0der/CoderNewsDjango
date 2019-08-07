import time

from django.http import HttpResponse
from coder_news.dataUpdate.NetworkSecurity import zol, zuori
from coder_news.dataUpdate.TechnologyArticles import appso, igao7, pcbeta, pconline, souhu, souhuArticles, sspaiArticles, sspaiSharingArticles

def update_technology():
    # zol.getZol()
    # zuori.getZuori()
    appso.getAppso()
    # igao7.getIgao7()
    # pcbeta.getPcbeta()
    # pconline.getPconline()
    # souhu.getSouhu()
    # time.sleep(3)
    # souhuArticles.getSouhuArticles()
    # sspaiArticles.getSspai()
    # sspaiSharingArticles.getSspai()
    return HttpResponse("Done!")