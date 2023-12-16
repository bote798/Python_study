# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   Test_function.py
# @Author  :   bote7
# @Date    :   2023/10/14 18:18
# @IDE     :   PyCharm

"""
     注意两个同辈的类被继承时,不能有相同的属性
        例如 Son1 和Son2 若同时有 miname 属性
           则被GrandSon类继承后，运行就会报错
"""


class Father:
    # 初始化方法
    def __init__(self, name, *args, **kwargs):
        """
        :param name:
        """
        """
            self 代表类的实例，
            name 代表类实例的属性。
            self.name = name 的含义是将参数 name 的值赋给 self 的 name 属性。
            这是一个简单的类属性赋值操作。
        """
        # 将属性name 传给 self.name
        self.name = name
        print("Father开始调用")
        print("Father的__init__结束调用")


# 继承父类 Father
class Son1(Father):
    # 初始化方法
    def __init__(self, name, age, *args, **kwargs):
        """
        :param name:
        :param age:
        """
        # 将属性 age 传给 self.age
        self.age = age
        print("Son1开始调用")
        # 获取父类（Father）的属性 name
        # 普通方式:
        # Father.__init__(self, name)
        # super方式:
        super().__init__(name, *args, **kwargs)
        print("Son1的__init__结束调用")


# 继承父类 Father
class Son2(Father):
    # 初始化方法
    def __init__(self, name, speak, *args, **kwargs):
        """
        :param name:
        :param speak:
        """
        # 将属性 speak 的值 传给 speak
        self.speak = speak
        print("Son2开始调用")
        # 获取父类（Father）的属性 name
        # 普通方式:
        # Father.__init__(self, name)
        # super方式:
        super().__init__(name, *args, **kwargs)
        print("Son2的__init__结束调用")


# 多继承父类 Son1 Son2
class GrandSon(Son1, Son2):
    # 初始化方法
    def __init__(self, name, age, speak):
        """
        :param name:
        :param age:
        :param speak:
        """
        print("GrandSon开始调用")

        # 获取父类（Son1）的属性 name age
        #        (Son2) 的属性 name speak
        # 普通方式:
        # Son1.__init__(self, name, age)
        # Son2.__init__(self, name, speak)
        # super方式（将继承的所有父类属性全部获取）:
        super().__init__(name, age, speak)
        print("GrandSon结束调用")

    def display(self):
        print(f"{self.name}{self.age}{self.speak}")


# 实例化对象(GrandSon类)
grandson = GrandSon("姓名  ", "年龄  ", "说话")
# 调用类方法
grandson.display()
# 查看GrandSon类的方法执行顺序
print(GrandSon.__mro__)
