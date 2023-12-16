# -*- coding: UTF-8 -*-
# @Project : PythonProjects 
# @File    : 协程_基础编写.py
# @Author  : bote798
# @Date    : 2023/11/1 20:10 
# @IDE     : PyCharm

import asyncio


# 并发任务
# 创建协程并发
async def work():
    print('任务开始')
    # 模拟IO
    await asyncio.sleep(2)
    print('任务结束')


# ------/创建主协程函数方式\------
"""
async def main():
    # 实例化task对象
    task = asyncio.create_task(work())
    result_1 = await task
    return result_1
    
# asyncio.run(main()) 在运行主协程函数的时候,run方法会创建一个事件循环对象
asyncio.run(main())
"""

# ------/不创建主方法\------
# 创建事件循环
loop = asyncio.new_event_loop()

# 创建task对象（实例化task对象）
# 1.
"""
task = loop.create_task(work())
print(type(task))  # <class '_asyncio.Task'>
# 将协程任务提交到事件循环中
loop.run_until_complete(task)
"""

# 2.
# 不要将tasks接传递到运行方法中
# 因为这里的task是一个列表对象,不是可等待对象
"""
    task = [loop.create_task(work()) for _ in range(5)]
    # task = [loop.create_task(work()) for _ in range(5)]
    # 等于:
    #   range(5) --->  0 1 2 3 4
    #   tasks = [
    #       loop.create_task(work()),
    #       loop.create_task(work()),
    #       loop.create_task(work()),
    #       loop.create_task(work()),
    #       loop.create_task(work())
    #   ]
    print(type(task))   # <class 'list'>
    loop.run_until_complete(task)
    loop.run_until_complete(asyncio.wait(task))
"""

"""
    asyncio.wait(task) 一次性将task所有的协程任务获取
    
    相同:
    从功能上看，asyncio.wait 和 asyncio.gather 实现的效果是相同的，都是把所有 Task 任务结果收集起来。
    
    不同:
    asyncio.wait 使用一个set保存它创建的Task实例，因为set是无序的所以这也就是我们的任务不是顺序执行的原因。
    会返回两个值：done 和 pending，done 为已完成的协程 Task，pending 为超时未完成的协程 Task，需通过 future.result 调用 Task 的 result；

    而asyncio.gather 返回的是所有已完成 Task 的 result，不需要再进行调用或其他操作，就可以得到全部结果
    如果列表中传入的不是create_task方法创建的协程任务，它会自动将函数封装成协程任务

"""
