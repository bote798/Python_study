# -*- coding: UTF-8 -*-
# @Project : TuLing 
# @File    : urls.py
# @Author  : bote798
# @Date    : 2023/12/14 16:55 
# @IDE     : PyCharm

from django.urls import path
from . import views
# 导入自定义转换器
from utils.converters import UsernameConverter, MobileConverter
urlpatterns = [
    path('usernames/<username:username>/count/', views.UsernameCountView.as_view()),
    path('mobiles/<mobile:mobile>/count/', views.MobileCountView.as_view()),
    path('register/', views.RegisterView.as_view()),
]
