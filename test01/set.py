# -*- coding:utf-8 -*-

"""
无需的
不可重复的
可变,可用于去重
"""

# 创建set
s1 = set()
print(s1)

# 空set不能这样定义
s2 = {}  # 这样得到的是一个字典
print(type(s2))

# 非空set可以这样定义并初始化
s3 = {"Tom", "Mike", "Jerry", "Tom"}
print(s3)
print(type(s3))

# 获取set的长度
print(len(s3))
# 使用in 或者 not in判断是否包含指定的元素
print("Tom" in s3)

# 判断两个set是否有交集

s4 = {"Tom"}
isdisjoint = s3.isdisjoint(s4)
print(isdisjoint)

# 并集
print(s3.union(s4))
print(s3 | s4)

# 求交集
print(s3.intersection(s4))
print(s3 & s4)

# 求差集
print(s3.difference(s4))
print(s3 - s4)

# 补集
print(s4.symmetric_difference(s3))
print(s4 ^ s3)

# 添加元素
s3.add("HH")
print(s3)

# 删除元素
s3.remove("HH")  # 如果没有这个元素,会报错
print(s3)
s3.clear()
print(s3)


# ============ 练习 ======================
import random

m = []
n = []
for i in range(10):
    m.append(random.randrange(10, 20))
    n.append(random.randrange(10, 20))
print(m, n)

print(set(m).union(set(n)))
print(set(m).intersection(n))
