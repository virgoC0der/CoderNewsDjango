from django.utils import timezone
from coder_news import models

class dataModel:

    def __init__(self,title,url,imageUrl,category):
        self.title = title
        self.url = url
        self.imageUrl = imageUrl
        self.category = category

    def printIt(self):
        print(self.title,self.url,self.imageUrl,self.category)


    def updateToInfo(self):
        self.date = timezone.now()
        models.Info.objects.create(title=self.title, url=self.url, imageURL=self.imageUrl, category=self.category, create_time=self.date)
        self.id = int(str(models.Info.objects.latest("id"))[13:-1])
        self.updateToChild()

    # 添加到子表
    def updateToChild(self):
        if self.category == "python":
            models.python.objects.create(create_time=self.date, infoId_id=self.id)
        if self.category == "java":
            models.Java.objects.create(create_time=self.date, infoId_id=self.id)
        if self.category == "swift":
            models.swift.objects.create(create_time=self.date, infoId_id=self.id)
        if self.category == "github":
            models.github.objects.create(create_time=self.date, infoId_id=self.id)
        if self.category == "Technology":
            models.techonology.objects.create(create_time=self.date, infoId_id=self.id)
        if self.category == "NetworkSecurity":
            models.networkSecurity.objects.create(create_time=self.date, infoId_id=self.id)

