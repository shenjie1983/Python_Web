'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2020-06-18 23:13:35
@LastEditors: 沈洁
@LastEditTime: 2020-07-14 21:25:01
'''
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def CalPage(request):
    return render(request, 'cal.html')


def Cal(request):
    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    result = int(value_a)+int(value_b)
    return render(request, 'result.html', context={'data': result})
    # print(value_a, value_b)
