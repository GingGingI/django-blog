from django.db import models
from django.template.context_processors import request
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


# Create your models here.

# 블로그 포스트 객체 생성
class Post(models.Model):
    authoor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class SignUp(request)