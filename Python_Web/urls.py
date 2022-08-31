'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2020-05-21 13:15:01
@LastEditors: 沈洁
@LastEditTime: 2020-07-28 14:35:00
'''
"""Python_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from firstWEB import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index)
    path('', views.index),
    path('calpage/', views.CalPage),
    path('cal', views.Cal)
]
