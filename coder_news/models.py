from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.TextField()
    preference = models.CharField(max_length=80, default="Github")


class Info(models.Model):
    title = models.TextField(max_length=500, unique=True)
    category = models.CharField(max_length=100)
    url = models.TextField()
    imageURL = models.TextField()
    create_time = models.DateField(default=timezone.now)
    like = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

class swift(models.Model):
    infoId = models.ForeignKey(Info,on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)

class python(models.Model):
    infoId = models.ForeignKey(Info,on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)

class Java(models.Model):
    infoId = models.ForeignKey(Info, on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)

class github(models.Model):
    infoId = models.ForeignKey(Info, on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)

class techonology(models.Model):
    infoId = models.ForeignKey(Info, on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)

class networkSecurity(models.Model):
    infoId = models.ForeignKey(Info, on_delete=models.CASCADE)
    create_time = models.DateField(default=timezone.now)

