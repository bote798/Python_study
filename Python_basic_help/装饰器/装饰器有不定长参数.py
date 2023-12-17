# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   装饰器有不定长参数.py
# @Author  :   bote798
# @Date    :   2023/10/17 17:55
# @IDE     :   PyCharm

def debug(func):
    def wrapper(*args, **kwargs):
        print(f'[debug:]{func.__name__}')
        print(args)
        for key,value in kwargs.items():
            print(f"{key}: {value}")

    return wrapper


@debug
def say_hello(*args, **kwargs):
    print(f'信息内容: {args}')


say_hello("hello", name="老刘 ", what="干嘛呢最近")
