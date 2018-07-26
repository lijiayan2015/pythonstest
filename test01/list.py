# -*- coding:utf-8 -*-
# 列表的定义
# 有序集合
# 可以存放不同的类型的数据
# 放在中括号中，有逗号分隔
cars = ['c++', 'java', 'android', 'ios']
print(type(cars))

print(cars)

numbers = list(range(10))
numbers1 = list(range(0, 10, 2))
print(numbers)
print(numbers1)

# 对数字列表的统计计算
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列表推导
vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])

# 求绝对值新列表
print([abs(x) for x in vec])

# 列表嵌套
vec1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for x in vec1 for num in x])

# 列表的常规操作
print(vec[0])
print(vec[-1])  # 返回的是一个元素
print(vec[:2])  # 返回的是一个列表

# 由于列表是可变的，所以可以通过索引修改索引对应的值
vec[1] = 1000
print(vec)

vec[1:3] = [10]
print(vec)  # [-4, 10, 2, 4]

vec[1:3] = [10, 20, 30, 40]
print(vec)  # [-4, 10, 20, 30, 40, 4]


# 列表的拼接
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list_total = list1 + list2
print(list_total)
print(list1 * 3)

# in 和 not in 关键字
print(1 in list1)
print(10 not in list1)

# 与字符串一样，没有会报错
# print(list1.index(100))

# 列表的修改
# 修改列表的元素值，单个或多个
# 添加一个元素
list = ['a', 'b', 'c', 'd', 'e']

list.append('fg')
list.extend('gh')
list.extend(['gh', 'ij', 'kl'])
print(list)

# 插入一个元素，如果是负数，且在负索引范围内，则在对应位置插入，如果没在索引范围内
# 则在头部插入
# 正索引也是同理
list.insert(-100, 'hello')
print(list)

# 删除元素
del list[1]

list.remove('hello')
print(list)

# 排序
print(list.sort())

list2 = [1, 2, 34, 45, 23, 566, 3]

# 排序，直接修改原列表，并没有生成新列表
# list2.sort()

copy = list2.copy()
copy.sort()

print(copy)
print(list2)

# sorted 返回一个新列表
newList2 = sorted(list2)
print(newList2)

# 对列表的遍历
for temp in list2:
    print(temp)

print("========while========")
i = 0
while i < len(list2):
    print(list2[i])
    i += 1
