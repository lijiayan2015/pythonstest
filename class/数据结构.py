__author__ = 'lijiayan'

"""
数据结构：
在逻辑上分为：
    线性结构：
        堆栈，队列
    非线性结构：
        树，图


"""
import time

start_time = time.time()
for i in range(1001):
    for j in range(1001 - i):
        for k in range(1001 - i - j):
            if (i + j + k == 1000) and (i ** 2 + j ** 2 == k ** 2):
                print(i, j, k)

end_time = time.time()

print(end_time - start_time)
