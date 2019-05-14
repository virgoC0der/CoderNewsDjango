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
    date = now().date() + timedelta(days=-5)
    if category == "python":
        id = list(models.python.objects.filter(create_time__startswith=date).values('id'))
    if category == "java":
        id = list(models.Java.objects.filter(create_time__startswith=date).values('id'))
    if category == "swift":
        id = list(models.swift.objects.filter(create_time__startswith=date).values('id'))
    if category == "github":
        id = list(models.github.objects.filter(create_time__startswith=date).values('id'))
    print(id)
    return int(str(id[0])[7:-1])
