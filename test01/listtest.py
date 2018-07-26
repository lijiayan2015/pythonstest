# -*- coding:utf-8 -*-

print("=" * 50)
print('名字关系系统')
print('1：添加一个新名字')
print('2：删除一个名字')
print('3：修改一个名字')
print('4：查询一个名字')
print('5：退出系统')
print("=" * 50)

list1 = []

num = 10
while False:
    number = input("请选择功能序号:")
    # num = int(number)
    if num == 1:
        name = input("请输入用户名：")
        list1.append(name)
        print(list1)
    elif num == 2:
        name = input("请输入要删除的名字:")
        list1.remove(name)
    elif num == 3:
        pass
    elif num == 4:
        pass
    else:
        break

print("==================逆序列表==============")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_ = list1[::-1]
print(list_)
copy = list1.copy()
copy.reverse()
print(copy)

# 过滤NaN
list2 = [1, 2.5, float('NaN'), 5.9, float('NaN')]

res_list = []
import math

for value in list2:
    if not math.isnan(value):
        res_list.append(value)

print(res_list)
