# -*- coding: UTF-8 -*-
# @Project : Python 
# @File    : 面试题 01.04. 回文排列.py
# @Author  : bote798
# @Date    : 2023/12/17 9:51 
# @IDE     : PyCharm
from collections import defaultdict

"""
    哈希表:
        哈希存储的基本思想是以关键字为自变量，通过一定的函数关系（称为散列函数或者哈希函数），
        计算出对应的函数值，以这个值作为数据元素的地址，将该数据元素存到相应的地址单元中去。
        查找时，再根据关键字采用计算哈希值的方式计算出相应的哈希地址，再到相应的存储单元去取需要的元素即可。
    
    字典
    key     为字母
    value   为存在的个数
    若字典中不存在该字母对应的key,则将其加入,并且使其为0
    若存在则将其个数(value)加1
    
    
"""
str_1 = "aaacsv"
h = {}
k = 0


def num(s):
    h = {}
    k = 0
    for i in s:
        if i not in h.keys():
            h[i] = 0
        else:
            h[i] += 1
    # print(h)
    for j in h.values():

        if (j % 2) == 0:
            k += 1

    """
        如果只有一个单独字母  'acoca'
            a: 1    1%2 = 1     k=0
            c: 1    1%2 = 1     k=0
            o: 0    0%2 = 0     k=1
            则k=1，return True
            
        若 字符串为: 'acocca'
            很明显不是回文,存在 o c 两个
                那么 c的value=2
                    first:  c:0
                    second: c:1
                    third:  c:2  --->   2%2=0 -->   k+1
                那么k=1（o）+1（c）=2
                    return False
            
    """
    if k > 1:
        return False
    else:
        return True


a = num

print(a(str_1))
