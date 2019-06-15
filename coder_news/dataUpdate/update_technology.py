from coder_news.dataUpdate.NetworkSecurity import zol, zuori
from coder_news.dataUpdate.TechnologyArticles import appso, igao7, pcbeta, pcbetaTech, pconline, souhu, souhuArticles, sspaiArticles, sspaiSharingArticles

def update_technology():
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