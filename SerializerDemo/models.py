from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(
        null=False,
        max_length=255,
        verbose_name='姓名'
    )
    age = models.IntegerField(
        null=False,
        verbose_name='年龄'
    )
    sex = models.IntegerField(
        null=False,
        verbose_name='性别'
    )
    active = models.BooleanField(
        # 默认值为 True
        default=True,
        verbose_name='是否活跃'
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='描述'
    )
