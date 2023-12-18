# -*- coding: UTF-8 -*-
# @Project : TuLing 
# @File    : converters.py
# @Author  : bote798
# @Date    : 2023/12/18 20:46 
# @IDE     : PyCharm
# 导入converters转换器包
from django.urls import converters, register_converter


# 自定义转换器
class UsernameConverter:
    # 使用正则表达式
    # a~z A~Z 0~9 _（下划线） -（破折号）
    """
        [a-zA-Z0-9_-]：这是一个字符集，用于匹配任何大小写字母（a-z, A-Z）、数字（0-9）、下划线（_）和破折号（-）。
        {5,20}：这是一个量词，表示前面的字符集至少重复5次，至多重复20次。
        换句话说，它要求匹配的字符串长度必须在5到20之间（包括5和20）。
    """
    regex = '[a-zA-Z0-9_-]{5,20}'

    # to_python: 将匹配结果传递给views视图层
    # to_url:    将匹配结果用于反向解析传值
    def to_python(self, value):
        return value


# 注册路由转换器
# 将转换器UsernameConverter功能赋给使用名username
# 该行代码写在这里和路由层都可以
register_converter(UsernameConverter, 'username')
