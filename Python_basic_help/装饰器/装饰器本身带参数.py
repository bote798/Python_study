# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   装饰器本身带参数.py
# @Author  :   bote798
# @Date    :   2023/10/17 19:10
# @IDE     :   PyCharm
def level(le):
    def debug(func):
        def wrapper(*args, **kwargs):
            print(f"[debug:]: {func.__name__}", le)
            # 将message（hello）传给 args
            func(*args, **kwargs)

        return wrapper

    return debug


@level('info')
def say_hello(message):
    print(f"信息:{message}")


say_hello("hello")
