from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    info = models.TextField(blank=True)
    age = models.IntegerField()
    company=models.CharField(max_length=200)