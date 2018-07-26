# -*- coding:utf-8 -*-
print("=" * 50)
print("名片管理系统")
print("1.添加一个新的名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示所有的名片")
print("6.退出系统")
print("=" * 50)

mingpian = []
num = 0
while True:
    num = int(input("请输入操作序号:"))

    if num == 1:
        d = {}
        # 相同名字的不能再新增
        name = input("请输入新的名字:")
        d['name'] = name
        qq = input("请输入QQ:")
        d['qq'] = qq
        weixin = input("请输入微信:")
        d['weixin'] = weixin
        address = input("请输地址:")
        d['address'] = address
        mingpian.append(d)
        continue
    if num == 2:
        name = input("请输入要删除的名片name:")
        for d in mingpian:
            if name in d.keys():
                mingpian.remove(d)
                break
    elif num == 3:
        name = input("请输入要修改的名片name:")
        for d in mingpian:
            if name in d.keys():
                name = input("请输入新的名字:")
                d['name'] = name
                qq = input("请输入QQ:")
                d['qq'] = qq
                weixin = input("请输入微信:")
                d['weixin'] = weixin
                address = input("请输地址:")
                d['address'] = address
                break
    elif num == 4:
        name = input("请输入要查询的名片name:")
        for d in mingpian:
            if name in d.keys():
                print(d)
                break
    elif num == 5:
        print(mingpian)

    else:
        break
