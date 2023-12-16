# -*- coding: UTF-8 -*-
# @Project : PythonProjects 
# @File    : 协程_绑定回调.py
# @Author  : bote798
# @Date    : 2023/11/2 8:30 
# @IDE     : PyCharm

import asyncio


async def work(message):
    print(1)
    return f'返回值为:{message}'


# 创建绑定回调时执行的函数
def callback(future):
    # future.result() 返回传进的函数的执行结果(返回值)
    # 这里返回的是 future ---> work('人才') 额就是work('人才')的返回值
    print('callback:', future.result())

# 实例化work方法
# 方便下面调用，一直打work("人才")太麻烦了


coro_obj = work("人才")

# 创建事件循环
loop = asyncio.new_event_loop()
# 创建task对象,存放任务
task = loop.create_task(coro_obj)
# 使用add.done_callback() 将callback方法绑定和task绑定
# 在task任务完成后,自动执行绑定的自定callback方法
task.add_done_callback(callback)
# 将任务提交到事件循环 loop 中
loop.run_until_complete(task)

