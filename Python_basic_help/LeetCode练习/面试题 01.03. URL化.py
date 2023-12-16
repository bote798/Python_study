# -*- coding: UTF-8 -*-
# @Project : Python 
# @File    : 面试题 01.03. URL化.py
# @Author  : bote798
# @Date    : 2023/12/16 21:27 
# @IDE     : PyCharm

"""
    输入的长度 lenth 是 字符串开头第一个字母到最后一个不为空格的字母的长度
    即:  Mr John Smith   ---> 13

    那么我们使用切片将最后一个字母后面的内容删除
    然后直接使用replace()进行替换即可
"""
str_1 = "Mr John Smith    "
lenth = 13

new_str_1 = str_1[:lenth]
print(new_str_1.replace(' ','%20'))
