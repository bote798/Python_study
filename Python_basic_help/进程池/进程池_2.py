# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   进程池_2.py
# @Author  :   bote798
# @Date    :   2023/10/24 20:15
# @IDE     :   PyCharm
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Pool
from random import random


def work_1(me_1, me_2):
    # 获取开始时间
    p_start = time.time()
    print(f'{me_1}开始执行,该子进程号为: {os.getpid()}，父线程PID: {os.getppid()}')
    print('me_2: ', me_2)
    # 设置进程等待时间
    time.sleep(random() * 2)
    # 设置结束时间
    p_stop = time.time()
    # 获取任务运行耗时(结束时间减去开始时间)
    print(f"程序执行完毕, 耗时: %.2f" % (p_stop - p_start))
    return me_2


# 进程必须写在主入口内
# 进程不能使用 start() 运行,只能通过主入口运行
if __name__ == '__main__':
    # 创建线程池对象
    # 设置最大进程数为 3 个

    """
    底层实现：ProcessPoolExecutor()使用concurrent.futures模块，而Pool()使用multiprocessing模块。
    
    ProcessPoolExecutor()是Python 3中的内置库，而Pool()是Python 2和3都可以使用的标准库。

    使用方式：ProcessPoolExecutor()是使用上下文管理器with语句来创建和管理进程池。
    
    在with语句块内，可以通过submit()方法提交任务，并使用result()方法获取任务结果。
    
    Pool()是通过实例化Pool对象来创建进程池，然后可以使用apply_async()或map()方法来提交任务。

    执行方式：ProcessPoolExecutor()使用ThreadPoolExecutor()来实现多线程，并在内部使用multiprocessing模块来创建进程池。
    
    这样可以更好的利用多核处理器的优势。而Pool()是直接使用multiprocessing.Pool对象来创建进程池。

    总的来说，ProcessPoolExecutor()是Python 3中推荐的多进程池实现，而Pool()是在Python 2和3都可以使用的多进程池。
    
    在Python 3中，如果只需要使用多进程池，并且不需要使用其他并发特性，推荐使用ProcessPoolExecutor()。
    """
    # 使用ProcessPoolExecutor()则不能使用close、join等功能
    # 关闭线程池绑定
    pool = ProcessPoolExecutor(max_workers=3)
    for i in range(10):
        pool.submit(work_1, i, '测试参数')

    # with ProcessPoolExecutor(max_workers=3) as pool:
    #     tasks = [pool.submit(work_1, i, '测试参数') for i in range(10)]
    #     for future in as_completed(tasks):
    #         print(future.result())
