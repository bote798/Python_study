# -*- coding: UTF-8 -*-
# @Project : 力扣 
# @File    : 面试题 01.06. 字符串压缩.py
# @Author  : bote798
# @Date    : 2023/12/18 9:12 
# @IDE     : PyCharm
import itertools

str_1 = "aabcccccaaa"

# 长度
lenth_1 = len(str_1)
"""
不推荐使用字符串直接 res += s[i] 拼接，
在 Python 中字符串是「不可变对象」，每次字符串拼接都会生成一个新字符串，效率低下。
推荐使用列表，先将结果按照顺序添加，最终返回前拼接为字符串，因此只需要一次拼接操作。
                            作者：Krahets
                            来源：力扣（LeetCode）
"""
list_1 = list()
i = 0
j = 0
# 计数器
count = 0
# i,j均不可超出字符串的长度
while i < lenth_1:
    while j < lenth_1 and str_1[i] == str_1[j]:
        # 如果i,j所指的字母相同,则计数器加1
        count = count + 1
        # j+1指向下一个字节
        j = j + 1
    # 若当前所指的两个字母不相同,则将之前i所指的字母与个数依次存入列表
    list_1.append(str_1[i])
    list_1.append(str(count))
    # 对计数器归零
    count = 0
    # 将j当前值赋给i,时i指向下一个不同的字母
    i = j
# 直接使用join将列表转为字符串
print(''.join(list_1))

# 正式解题
# i, j, lenth = 0, 0, len(S)
# list_1 = list()
# while i < lenth:
#     while j < lenth and S[i] == S[j]:
#         j = j + 1
#     list_1.append(S[i])
#     # j与i的差值就是字母数量（这样省去了计数器）
#     list_1.append(str(j - i))
#     i = j
# new_str = ''.join(list_1)
# 题目的最后一个要求,压缩后的长度小于原字符串,则输出,否则输出原字符串
# return new_str if len(new_str) < lenth else S


"""
    使用itertools.groupby(iterable, key=None):
        itertools.groupby 是 Python 标准库中的一个函数，它允许你根据指定的键对可迭代对象进行分组。
        它的作用是将相邻的元素分组为一个子序列，其中每个子序列都具有相同的键值。
"""
# [*v]: 将v转为列表

s = min(str_1, "".join(k + str(len(list(v))) for k, v in itertools.groupby(str_1)), key=len)
print(s)
# 将其拆解,先做一个列表,作用和上面的相同
z = []

# 字符串: "aabcccccaaa"
# itertools.groupby(str_1): aa,b,ccccc,aaa (将相同的元素分组)
# 使用for遍历出数据
for k, v in itertools.groupby(str_1):
    # 将其依次加入到列表中
    z.append(k + str(len(list(v))))
#  转为字符串输出,并且使用min()判断长度
print(min(str_1, ''.join(z)))
