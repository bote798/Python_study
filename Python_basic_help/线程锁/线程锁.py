# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   线程锁.py
# @Author  :   bote798
# @Date    :   2023/10/23 19:46
# @IDE     :   PyCharm
import threading
from threading import Thread, RLock

num = 0
rlock = RLock()


def add():
    # global 将num变为全局变量
    global num
    for i in range(1000):
        rlock.acquire()  # 上锁
        num += 1
        rlock.release()  # 解锁


def sub():
    global num
    for i in range(1000):
        rlock.acquire()  # 上锁
        num -= 1
        rlock.release()  # 解锁


# 创建线程对象
# t1 = threading.Thread() 与 t1 = Thread()类似 , 但Thread缺少一些线程管理功能
t1 = Thread(target=add)
t2 = Thread(target=sub)
# 开启线程
t1.start()
t2.start()
print(num)
