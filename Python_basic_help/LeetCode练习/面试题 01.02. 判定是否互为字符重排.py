# -*- coding: UTF-8 -*-
# @Project : Python 
# @File    : 面试题 01.02. 判定是否互为字符重排.py
# @Author  : bote798
# @Date    : 2023/12/16 21:00 
# @IDE     : PyCharm

# 使用sorted将乱序的字符串排序（同时会将其转为list类型）
# 存在两个字符串都是乱序的情况

str_1 = "abcde"
str_2 = "acedb"

print(sorted(str_1)==sorted(str_2))
