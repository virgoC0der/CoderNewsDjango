from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.TextField()
    preference = models.CharField(max_length=80, default="Github")


class Info(models.Model):
    title = models.CharField(max_length=128, unique=True)
    category = models.CharField(max_length=50)
    url = models.URLField(max_length=100, unique=True)
    imageURL = models.URLField(max_length=256, default=None, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    like = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

