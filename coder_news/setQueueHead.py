from django.utils.timezone import now, timedelta
from coder_news.views import split_data
from coder_news import models
from django.http import HttpResponse,JsonResponse

def set_queue_head(request):
    categoryJSON = request.GET.get("categoryArray", '')
    categoryJSON = split_data(categoryJSON)
    queueHeadArray = {}
    for category in categoryJSON:
        queueHeadArray[category] = int(get_info(category)[7:-1])
    return JsonResponse(queueHeadArray)


def get_info(category) -> str:
    date = now().date() + timedelta(days=-1)
    if category == "python":
        id = list(models.python.objects.filter(create_time__startswith=date).values('id'))
    if category == "swift":
        id = list(models.swift.objects.filter(create_time__startswith=date).values('id'))
    return str(id[0])
