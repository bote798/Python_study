# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   迭代器_整合模式.py
# @Author  :   bote7
# @Date    :   2023/10/15 19:08
# @IDE     :   PyCharm

class MyList:

    def __init__(self):
        # 创建列表
        self.list = list()

        # 计数器
        self.count = 0

    def add(self, value):
        self.list.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.list):
            item = self.list[self.count]
            self.count += 1
            return item
        else:
            # 手动抛出异常
            raise StopIteration


if __name__ == '__main__':
    # 实例化对象
    my_list = MyList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)

    # 创建迭代器对象
    iter_obj = iter(my_list)
    print(next(iter_obj))
