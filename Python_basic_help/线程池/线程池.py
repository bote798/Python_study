# -*- coding :UTF-8 -*-
# @Project :   Projects
# @File    :   线程池.py
# @Author  :   bote7
# @Date    :   2023/10/23 20:12
# @IDE     :   PyCharm

import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait

import requests


def get_image(url):
    """
        requests.get(url)   方法获取URL的响应
        response.content    获取响应的网页内容
    """
    response = requests.get(url).content
    # 提取文件名
    file_name = url.rsplit('/')[-1]
    with open(file_name, 'wb') as f:
        f.write(response)
        time.sleep(1)
        print("下载完成...")
    return response


# 创建线程池对象(最大线程为2)
pool_1 = ThreadPoolExecutor(max_workers=2)

url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg'
]

# for img_url in url_list:
#     # submit()用于提交任务，并且返回类型为future类型的值
#     future = pool_1.submit(get_image, img_url)
#     # result()用于获取所有任务的返回值，并且在所有任务完成后一起返回
#     print(future.result())

# 将所有任务的返回值存储在 列表 all_task中
# all_task = [pool_1.submit(get_image, img_url) for img_url in url_list]
#
# as_completed(all_task)  # 返回一个迭代器
# # 获取所有返回值,然后一次性提交
# for future in as_completed(all_task):
#     print(future.result())

# map可以提交任务,当前任务的参数可以使用迭代对象进行传递
# for res in pool_1.map(get_image, url_list):
#     pass

all_task = [pool_1.submit(get_image, img_url) for img_url in url_list]
# 运行线程池后
# wait()让主线程阻塞,等待所有任务完成后接着运行
wait(all_task)
print("主线程结束运行...")
