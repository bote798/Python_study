# -*- coding: UTF-8 -*-
# @Project : Python 
# @File    : 面试题 01.01. 判定字符是否唯一.py
# @Author  : bote798
# @Date    : 2023/12/16 20:30 
# @IDE     : PyCharm

"""
    set解释:
        set是一种集合数据类型，表示一个无序且不重复的集合。
        set()方法可以用于创建一个空的集合，也可以将其他可迭代对象转换为集合。
        与其他Python数据类型不同，
        set没有索引，不能通过索引访问其元素，但可以使用一些方法来操作和访问集合中的元素。
"""
# 集合是一个无序的不重复元素序列。

repeat_str = "ascdefghijklmnopqq"
no_repeat_str = "ascdefghijklmnopq"
sets = set(repeat_str)
sets_1 = set(no_repeat_str)
print(type(sets))  # <class 'set'>
print(sets)
print(sets_1)
# 由以上的两个输出结果可见两个set集合的元素数量相同,所以重复的元素在转为集合后被去除了

"""
    接下来我们简化一下代码
    因为去除重复前与去除重复后的长度不同
    所以我们只需要比对长度即可
"""
astr = "asceqq"  # 设定题目所给字符串
sets = set(astr)
if len(sets) == len(astr):
    print('True')
else:
    print('False')
# 还是很繁琐,继续简化
# 因为系统进行比对后，会返回True或False，所以只需要一句即可
print(len(astr)==len(set(astr)))    # 答题时替换为return即可

