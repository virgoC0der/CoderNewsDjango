from coder_news import models
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
import random
import string


def add_user(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    password_crypted = make_password(password, 'pbkdf2_sha256')
    print(password_crypted)
    try:
        models.User.objects.create(username=username, password=password_crypted)
    except:
        return HttpResponse("用户名已存在！")
    return HttpResponse("username="+username+"password"+password)


def login(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    print(username)
    print(password)
    try:
        usr = models.User.objects.get(username__exact=username)
        if check_password(password, usr.password):
            return HttpResponse("登录成功")
    except:
        return HttpResponse("用户名或密码错误！")
    # return HttpResponse("登录成功！")


def find_topic(request):
    category = request.GET.get('categoryArray', '')
    category = category.split(",")
    amount = int(request.GET.get('infoAmount', ''))
    read_info = request.GET.get('readInfo', '')
    read_num = request.GET.get('readNum', '')
    read_info = read_info.replace('[', '')
    read_info = read_info.replace(']', '')
    read_info = read_info.split(",")
    read_num = read_num.replace('[', '')
    read_num = read_num.replace(']', '')
    read_num = read_num.split(",")
    print(read_info)
    r = random.randint(1, 150)
    print(r)
    count = int(amount/len(category))
    news = {"list": []}
    i = 1
    for cat in category:
        print(cat)
        if i == len(category):
            # print(i)
            topic = models.Info.objects.filter(category__contains=cat)[r:amount-count*(i-1)+r].values("title", "url", "imageURL", "category")
        else:
            topic = models.Info.objects.filter(category__contains=cat)[r:r+count].values("title", "url", "imageURL", "category")
        news["list"].append(list(topic))
        r += count
        print(topic.values("id"))
        i += 1
    return JsonResponse(news, json_dumps_params={'ensure_ascii': False}, safe=False)
    # return HttpResponse('topic:'+topic.topic+'\nurl:'+topic.url)

