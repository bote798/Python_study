# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   Test_function3.py
# @Author  :   bote7
# @Date    :   2023/10/14 22:06
# @IDE     :   PyCharm
class Father:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        print("开始调用  Father")
        print("结束调用Father")


class Son1(Father):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        print("开始调用  Son1")
        super().__init__(name, *args, **kwargs)
        print("结束调用Son1")


class Son2(Father):
    def __init__(self, name, gender, *args, **kwargs):
        self.gender = gender
        print("开始调用  Son2")
        super().__init__(name, *args, **kwargs)
        print("结束调用Son2d")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print("开始调用  GrandSon")
        super().__init__(name, age, gender)
        print("结束调用GrandSon")


# 实例化对象类
grandson = GrandSon("name ", "age ", "gender")
# 查看 类的方法调用顺序
print(GrandSon.__mro__)
