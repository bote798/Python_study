# -*- coding: UTF-8 -*-
# @Project : PythonProjects 
# @File    : 协程与线程和进程的交叉练习.py
# @Author  : bote798
# @Date    : 2023/11/1 21:34 
# @IDE     : PyCharm

import time
import asyncio
import concurrent.futures


def work():
    # 子进程要执行的代码
    print(1)
    time.sleep(1)  # IO任务
    return '返回值'


# 创建主协程函数
async def main():
    # 创建事件循环
    loop = asyncio.new_event_loop()

    # 使用上下文管理器with创建线程池
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        # 将
        result = await loop.run_in_executor(pool, work)
    print(result)


# 进程只能放在__main__中执行
if __name__ == '__main__':
    # 运行主协程方法
    asyncio.run(main())
