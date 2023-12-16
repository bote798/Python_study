# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   进程池_1.py
# @Author  :   bote7
# @Date    :   2023/10/24 20:58
# @IDE     :   PyCharm
import time
from multiprocessing import Pool
from random import random


def work(message):
    # 设置进程等待时间（此处使用random() 随机等待时间）
    time.sleep(random() * 2)
    print(message)


if __name__ == '__main__':
    # 创建进程池对象 个数为 3
    pool = Pool(3)

    for i in range(10):
        # 设置异步执行
        pool.apply_async(work, args=(i,))
        # 同步执行
        # pool.apply(work, args=(i,))

    # 关闭进程池
    pool.close()
    # 阻塞主进程,等待子进程完成再继续执行主进程
    pool.join()
