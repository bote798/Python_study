# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   闭包.py
# @Author  :   bote798
# @Date    :   2023/10/16 14:13
# @IDE     :   PyCharm

def external(num=0):
    def internal(message):
        """
            关键字 nonlocal 可以将不可修改的外部形参 num 变得内部可修改
            若外部的 num 不给值,则下面的 external(1)括号中必须给值
            若给了默认值,则下面的external(1)括号中不给值时,程序按照默认值运行
        """
        nonlocal num
        num += 1
        print("闭包internal函数输出")
        print(f"{num},{message}")

    print("闭包external函数输出")
    return internal


# 将闭包内部internal方法的地址赋值给 ex
ex = external(1)  # 输出 闭包external函数输出

ex("信息输出...")  # 输出 闭包internal函数输出
"""
    输出结果为:  
            闭包external函数输出
            闭包internal函数输出
            
    ex = external() 输出  闭包external函数输出
    ex()            输出  闭包internal函数输出
    
    所以很显然 
        external() 会运行闭包的外部函数,然后将返回的内部方法的地址传给 ex
        ex()就会运行闭包的内部函数
"""
