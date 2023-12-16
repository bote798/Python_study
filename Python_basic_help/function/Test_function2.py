# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   Test_function2.py
# @Author  :   bote7
# @Date    :   2023/10/14 20:10
# @IDE     :   PyCharm

class Father:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        print("开始调用Father")
        print("结束调用Father")


class Son1(Father):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        print("开始调用Son1")
        super().__init__(name, *args, **kwargs)
        print("结束调用Son1")


class Son2(Father):
    def __init__(self, name, speak, *args, **kwargs):
        self.speak = speak
        print("开始调用Son2")
        super().__init__(name, *args, **kwargs)
        print("结束调用Son2")


# 多继承 Son1 Son2
class GrandSon(Son1, Son2):
    def __init__(self, name, age, speak, *args, **kwargs):
        print("开始调用GrandSon")
        super().__init__(name, age, speak, *args, **kwargs)
        print(f"{self.name}{self.age}{self.speak}")
        # print “多了” "s"
        for arg in args:
            print(arg)
        # print why: 1
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        print("结束调用GrandSon")


# 实例化对象
grandson = GrandSon("李", "18", "走吧", "多了", "s", why=1)

# 查看GrandSon类的方法执行顺序
print(GrandSon.__mro__)
