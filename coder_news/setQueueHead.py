from django.utils.timezone import now, timedelta
from coder_news.views import split_data
from coder_news import models
from django.http import HttpResponse, JsonResponse


# 设置查询数据队首id
def set_queue_head(request):
    categoryJSON = request.GET.get("categoryArray", '')
    categoryJSON = split_data(categoryJSON)
    queueHeadArray = {}
    for category in categoryJSON:
        queueHeadArray[category] = get_info(category)
    return JsonResponse(queueHeadArray)


# 获取前一天日期的id起点
def get_info(category) -> int:
    i = -5
    date = now().date() + timedelta(days=i)
    print(date)
    id = None
    while id == None:
        if category == "python":
            try:
                id = models.python.objects.filter(create_time__startswith=date).first().id
            except:
                i -= 1
                date = now().date() + timedelta(days=i)
        if category == "java":
            try:
                id = models.Java.objects.filter(create_time__startswith=date).first().id
            except:
                i -= 1
                date = now().date() + timedelta(days=i)
        if category == "swift":
            try:
                id = models.swift.objects.filter(create_time__startswith=date).first().id
            except:
                i -= 1
                date = now().date() + timedelta(days=i)
        if category == "github":
            try:
                id = models.github.objects.filter(create_time__startswith=date).first().id
            except:
                i -= 1
                date = now().date() + timedelta(days=i)
        if id != None:
            break
    return id
