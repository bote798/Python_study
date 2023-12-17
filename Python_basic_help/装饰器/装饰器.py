# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   装饰器.py
# @Author  :   bote798
# @Date    :   2023/10/17 17:14
# @IDE     :   PyCharm

def debug(func):
    def wrapper():
        print(f"[Debug:]{func.__name__}")
        func()

    return wrapper


def say_hello():
    print("hello")


if __name__ == '__main__':
    """
        将函数hello的地址赋值给H
    """
    H = say_hello
    # H() = hello()
    # 将hello函数传给debug后
    # 将debug中的wrapper函数地址 赋值 给 H
    H = debug(H)
    H()
