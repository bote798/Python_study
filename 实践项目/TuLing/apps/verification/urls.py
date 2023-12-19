# -*- coding: UTF-8 -*-
# @Project : TuLing 
# @File    : urls.py
# @Author  : bote798
# @Date    : 2023/12/19 19:09 
# @IDE     : PyCharm

from django.urls import path
from . import views
# 导入自定义转换器
from utils.converters import UUIDConverter

urlpatterns = [
    path('image_codes/<uuid:uuid>/', views.ImageCodeView.as_view()),
]
