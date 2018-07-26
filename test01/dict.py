# -*- coding:utf-8 -*-

# 字典:
"""
    无序,键值对的集合
    字典中的元素通过键取值
    键要求不能重复,是不可变的数据类型,键唯一
"""

# 创建空字典
dict1 = {}
print(type(dict1))

dict1['one'] = '张三'
print(dict1)

dict1['two'] = 2
dict1[2] = 'python'
dict1[2] = 'python1'  # 修改已经存在key的值
print(dict1)

d1 = dict(one=1, two=2, three=3)
print(d1)

d2 = {"one": 1, "two": 2, "three": 3}
print(d2)

# 通过拉链操作创建字典
d3 = dict(zip(["one", "two", "three", "four"], [1, 2, 3, 4]))
print(d3)

# 通过元组列表创建字典
d4 = dict([('one', 1), ("two", 2), ("three", 3)])
print(d4)

d5 = dict({'one': 1, 'two': 2, 'three': 3})
print(d5)

# 使用列表推导
d6 = {x: x ** 2 for x in range(1, 10)}
print(d6)

# 访问字典
print(d5['one'])  # 如果键不存在,将会报错
print(d5.get('one1', 100))  # 如果键不存在,没有给默认值,返回None,给了默认值,返回默认值

keys = d5.keys()
print(type(keys))
print(type(d5.values()))

for key in keys:
    print(key)

# 字典的常用操作
d5['one'] = 'i'  # 如果键不存在,添加,如果键存在且值不同,则对值进行修改

# 删除元素
del d5['one']  # 如果键不存在,则会报错
print(d5)

d5.pop('two')  # 如果键不存在,则会报错
print(d5)

# 随机删除元素
d5.popitem()

print(d5)

# 返回字典的长度(键值对个数)
print(len(d5))

# 返回字典中所有项,键值对以元组返回
print(d4.items())

# in 或者 not in
print('one' in d4)

# 遍历所有的键
for tmp in d4.keys():
    print(tmp)
# 遍历所有的值
for tmp in d4.values():
    print(tmp)

for (k, v) in d4.items():
    print(k, v)
