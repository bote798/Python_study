# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   装饰器语法糖.py
# @Author  :   bote798
# @Date    :   2023/10/17 17:34
# @IDE     :   PyCharm

def debug(func):
    def wrapper():
        print(f"[debug:]{func.__name__}")
        func()

    return wrapper


@debug
def say_hello():
    print("hello")


say_hello()
