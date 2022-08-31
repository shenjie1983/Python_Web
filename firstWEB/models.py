'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2020-06-18 23:13:35
@LastEditors: 沈洁
@LastEditTime: 2020-08-03 13:30:40
'''
from django.db import models

# Create your models here.


class cal(models.Model):
    value_a = models.CharField(max_length=10)
    value_b = models.FloatField(max_length=10)
    result = models.CharField(max_length=10)
    
