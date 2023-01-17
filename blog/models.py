from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #글자 수가 제한된 텍스트를 정의할 때 사용
    text = models.TextField() #글자 수에 제한이 없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(
        default=timezone.now) #날짜와 시간을 의미
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save
    
    def __str__(self):
        return self.title