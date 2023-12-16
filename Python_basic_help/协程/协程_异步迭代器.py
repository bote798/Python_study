# -*- coding: UTF-8 -*-
# @Project : PythonProjects 
# @File    : 协程_异步迭代器.py
# @Author  : bote798
# @Date    : 2023/11/1 22:01 
# @IDE     : PyCharm

import asyncio


# 创建类
class Reader:
    def __init__(self):
        # 计数器
        self.count = 0

    async def read_line(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        # 返回一个迭代器对象 实例对象
        return self

    async def __anext__(self):
        # 定义迭代的具体过程
        value = await self.read_line()
        if value is None:
            # 手动抛出异常
            raise StopAsyncIteration
        return value


# 创建主协程函数
async def main():
    async for i in Reader():
        print(i)


asyncio.run(main())
