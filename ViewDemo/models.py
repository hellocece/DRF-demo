from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=255,
        verbose_name='姓名'
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='年龄'
    )
    time_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='加入时间'
    )
