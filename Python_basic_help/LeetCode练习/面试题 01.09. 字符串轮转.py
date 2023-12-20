# -*- coding: UTF-8 -*-
# @Project : 力扣 
# @File    : 面试题 01.09. 字符串轮转.py
# @Author  : bote798
# @Date    : 2023/12/20 8:47 
# @IDE     : PyCharm

"""
    注意:
        所有带翻转的,都可以尝试将原数组复制一倍解决
    题目要点:
        s1  s2
        字符串长度相同
        同一字母数量相同
        s2是s1字符串的部分字符翻转而成
        例子: s1: waterbottle
             s2: erbottle wat
            这里的s2就是由s1前部分的wat翻转到后面而成的

        思路:
            那么只是头尾部分翻转变化,我们就可以看出若将翻转的部分放回前面就是原字符串
            那么我们通过将两个s2字符串拼接,实现头尾重接
            那么再验证s1是否在拼接后的字符串中即可
            例子:
                erbottlewaterbottlewat
                erbottle waterbottle wat
                很明显,拼接后的字符串中包含s1那么证明s2是s1翻转后的结果
"""
# 代码实现
s1 = "waterbottle"
s2 = "erbottlewat"
# 先做长度验证
if len(s1) == len(s2):
    # 长度相同
    # 验证s1是否在拼接后的字符串中
    if s1 in (s2 + s2):
        # 在为 True
        print('True')
    else:
        # 不在 False
        print('False')
else:
    # 长度不同 False
    print('False')

# 然后正式解答
# return len(s1) == len(s2) and s1 in (s2 + s2)
