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
    return HttpResponse("username=" + username + "password" + password)


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
    # 获取数据
    categoryJSON = request.GET.get('categoryArray', '')
    amount = int(request.GET.get('infoAmount', ''))
    queueHeadArrayJSON = request.GET.get('queueHeadArray', '')
    categoryArray = split_data(categoryJSON)
    queueHeadArray = split_data(queueHeadArrayJSON)

    # 对每个数据源进行分配
    baseAmount = int(amount / len(categoryArray))
    categoryGetInfoAmountArray = []  # 每个数据源需要获取的量
    if baseAmount == 0:
        # 处理数据源大于数据量的情况
        gap = len(categoryArray) - amount
        for i in range(0, gap):
            randomInt = random.randint(0, len(categoryArray) - 1)
            del (categoryArray[randomInt])
        for index in range(0, len(categoryArray)):
            categoryGetInfoAmountArray.append(1)
        print(categoryGetInfoAmountArray)
    else:
        # 随机添加在某一个项里
        extendAmount = amount % len(categoryArray)
        randomIndex = random.randint(0, len(categoryArray) - 1)
        for index in range(0, len(categoryArray)):
            if randomIndex == index:
                categoryGetInfoAmountArray.append(baseAmount + extendAmount)
            else:
                categoryGetInfoAmountArray.append(baseAmount)
        print(categoryGetInfoAmountArray)
    # 根据队首获取信息
    result = {"data": []}
    # 检测要获取数据数目大于总数
    for index in range(0, len(categoryArray) - 1):
        categoryCount = categoryGetInfoAmountArray[index]
        queueHead = int(queueHeadArray[index])
        category = categoryArray[index]
        categoryAmount = getCategoryAmount(category)
        temp = categoryCount
        print(categoryCount)
        if categoryCount + queueHead - 1 > categoryAmount:
            categoryCount = categoryAmount - queueHead + 1
            categoryGetInfoAmountArray[index + 1] += temp - categoryCount
            print(categoryGetInfoAmountArray[index + 1])
            if categoryCount < 0:
                categoryCount = 0
    i = 1
    for index in range(0, len(categoryArray)):
        categoryName = categoryArray[index]
        categoryCount = categoryGetInfoAmountArray[index]
        queueHead = int(queueHeadArray[index])
        infoDataArray = getInfo(categoryName, queueHead, categoryCount)
        if i > 1:
            infoDataArray = checkRepeat(infoDataArray, result["data"], categoryName, queueHead)
        result["data"].extend(infoDataArray)
        i += 1
    # 组装信息
    resultForJson = getAJsonRespondWithDict(result)
    # 返回信息
    return resultForJson

# 通过url查找
def find_by_url(request):
    url_list = request.GET.get('urlList', '')
    url_list = split_data(url_list)
    print(url_list)
    result = {"data": []}
    for index in url_list:
        print(index)
        infoDataArray = list(models.Info.objects.filter(url=index).values('title', 'url', 'imageURL', 'category', 'like', 'id'))
        result["data"].extend(infoDataArray)
    # 组装信息
    resultForJson = getAJsonRespondWithDict(result)
    return resultForJson

def getInfo(category, queueHead, count):
    datas = None
    if category == "python":
        datas = models.python.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "java":
        datas = models.Java.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "swift":
        datas = models.swift.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "computer" or category=="Technology" or category == "phone":
        datas = models.techonology.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "NetworkSecurity" or category == "networkSecurity":
        datas = models.networkSecurity.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "phone" or category == "Phone":
        datas = models.phone.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "computer" or category == "Computer":
        datas = models.computer.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "TechnologyArticles":
        datas = models.articles.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "ResourceRecommend":
        datas = models.recommand.objects.filter(id__range=(queueHead, queueHead + count - 1))
    if category == "AppSolution":
        datas = models.appsolution.objects.filter(id__range=(queueHead, queueHead + count - 1))
    # 把子表转换为主表数据集合\
    infoData = list(
        datas.values('infoId__title', 'infoId__url', 'infoId__imageURL', 'infoId__category', 'infoId__like', 'infoId'))
    return infoData


def split_data(data):
    data = data.replace("[", '')
    data = data.replace("]", '')
    data = data.split(",")
    return data


# 辅助方法
def getValue(request, name):
    return request.GET.get(name)


# 结果查重
def checkRepeat(infoDataArray, resultJson, category, queueHead):
    index = 0
    head = queueHead + len(infoDataArray)
    while (index < len(infoDataArray)):
        infoId = infoDataArray[index]["infoId"]
        for result in resultJson:
            # 如果重复，查找下一条数据
            if result["infoId"] == infoId:
                del (infoDataArray[index])
                index -= 1
                infoDataArray += getInfo(category, head, 1)
                head += 1
                break
        index += 1
    return infoDataArray


# 获取该分类信息数目
def getCategoryAmount(category) -> int:
    amount = None
    if category == "swift":
        amount = int(str(models.swift.objects.latest("id"))[14:-1])
    if category == "python":
        amount = int(str(models.python.objects.latest("id"))[15:-1])
    if category == "java":
        amount = int(str(models.Java.objects.latest("id"))[13:-1])
    if category == "github":
        amount = int(str(models.github.objects.latest("id"))[15:-1])
    if category == "Technology" or category == "computer" or category == "phone":
        amount = int(str(models.techonology.objects.latest("id"))[20:-1])
    if category == "NetworkSecurity" or category == "networkSecurity":
        amount = int(str(models.networkSecurity.objects.latest("id"))[24:-1])
    if category == "Phone" or category == "phone":
        amount = int(str(models.phone.objects.latest("id"))[14:-1])
    if category == "Computer" or category == "computer":
        amount = int(str(models.computer.objects.latest("id"))[17:-1])
    if category == "TechnologyArticles":
        amount = int(str(models.articles.objects.latest("id"))[17:-1])
    if category == "AppSolution":
        amount = int(str(models.appsolution.objects.latest("id"))[20:-1])
    if category == "ResourceRecommend":
        amount = int(str(models.recommand.objects.latest("id"))[18:-1])
    return amount
