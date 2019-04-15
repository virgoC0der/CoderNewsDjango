from coder_news import models
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
import random
from .JsonStringChanger import *

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

    #获取数据
    categoryJSON = request.GET.get('categoryArray', '')
    amount = int(request.GET.get('infoAmount', ''))
    queueHeadArrayJSON = request.GET.get('queueHeadArray', '')
    categoryArray = split_data(categoryJSON)
    queueHeadArray = split_data(queueHeadArrayJSON)

    #对每个数据源进行分配
    baseAmount = amount/len(categoryArray)
    categoryGetInfoAmountArray = []#每个数据源需要获取的量
    if baseAmount == 0 :
        #处理数据源大于数据量的情况
        pass
    else:
        #随机添加在某一个项里
        extendAmount = amount%len(categoryArray)
        randomIndex = random.randint(0,len(categoryArray)-1)
        for index in range(0,len(categoryArray)-1):
            if randomIndex == index :
                categoryGetInfoAmountArray.append(baseAmount+extendAmount)
            else:
                categoryGetInfoAmountArray.append(baseAmount)
    #根据队首获取信息
    result = {"data":[]}
    for index in range(0,len(categoryArray)):
        categoryName = categoryArray[index]
        categoryCount = categoryGetInfoAmountArray[index]
        queueHead = queueHeadArray[index]
        infoDataArray = getInfo(categoryName,queueHead,categoryCount)
        result["data"].extend(infoDataArray)
    #组装信息
    resultForJson = getAJsonRespondWithDict(result)
    #返回信息
    return resultForJson

def getInfo(category,queueHead,count):
    if category == "Github":
        datas = models.Github.objects.filter(id__range=(queueHead,queueHead+count))
    #把子表转换为主表数据集合
    infoData = []
    for data in datas:
        infoData.append(data.infoId)
    return infoData


def split_data(data):
    data = data.replace("[", '')
    data = data.replace("]", '')
    data = data.split(",")
    return data

#辅助方法

def getValue(request, name):
    return request.GET.get(name)
