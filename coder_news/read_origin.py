from django.utils.timezone import now, timedelta
from coder_news.views import split_data
from coder_news import models
from django.http import HttpResponse,JsonResponse

def init_read_origin(request):
    category = request.GET.get("category", '')
    category = split_data(category)
    date = now().date() + timedelta(days=-1)
    read_num = {}



