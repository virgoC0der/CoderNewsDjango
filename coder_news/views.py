from coder_news import models
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password


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
    amount = int(request.GET.get('infoAmount', ''))
    read_info = request.GET.get('readInfo', '')
    read_num = request.GET.get('readNum', '')
    category = split_data(category)
    read_info = split_data(read_info)
    read_num = split_data(read_num)
    read = {}
    for info in read_info:
        for num in read_num:
            read[info] = int(num)
    print(read)
    # print(r)
    count = int(amount/len(category))
    news = {"list": []}
    i = 1
    for cat in category:
        print(cat)
        if i == len(category):
            # print(i)
            topic = models.Info.objects.filter(category__contains=cat)[read[cat]:amount-count*(i-1)+read[cat]].values("title", "url", "imageURL")
        else:
            topic = models.Info.objects.filter(category__contains=cat)[read[cat]:read[cat]+count].values("title", "url", "imageURL")
        news["list"].append(list(topic))
        print(topic.values("id"))
        i += 1
    return JsonResponse(news, json_dumps_params={'ensure_ascii': False}, safe=False)


def split_data(data):
    data = data.replace("[", '')
    data = data.replace("]", '')
    data = data.split(",")
    return data
