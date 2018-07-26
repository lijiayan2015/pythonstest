# -*- coding:utf-8 -*-
# 声明一个变量
a = 10
# 删除一个变量
del a

# print(a)

# 序列
# 常用的序列：str，list，tuple，dict，array
# 分为可变序列与不可变序列

# 定义字符串
str1 = "你好"

str2 = '你好'

str3 = "你好啊\n小伙子"

str4 = r"你好啊小伙子"
print(str3, str4)

# 判断两个字符串是否相等
print(id(str1), id(str2))
# 字符串比较短的时候创建一个一样的对象，如果长度达到一定的值，则会创建两个不一样的对象

str5 = 'abc'
str6 = str5
str5 = 'efg'
print(str5, str6)

str7 = 'abcdefg'
# 字符串 a  b  c   d  e
# 正索引 0  1  2   3  4
# 负索引-5  -4 -3  -2 -1
print(str7[0])
print(str7[-1])
# 注意，字符串是不可变序列，不能通过索引更改某个位置的值

# 取子串
print(str7[0:3])  # 取出0-3位置的子串
print(str7[:3])  # 取出0-3位置的子串
print(str7[1:-1])  # 取出第一个到不包括最后一个字符的子串
print(str7[1:])  # 取出1到最后一个字符子串
print(str7[:])  # 取出所有字符

# 字符串拼接
str1 = 'hello'
str2 = 'world'
print(str1 + str2)
print(str2 * 10)  # 输出10遍

# in 关键字判断一个字符串是否在另一个字符串中
str1 = 'abc'
str2 = "abcdef"
print(str1 in str2)
print(str1 not in str2)

# 字符串格式化
name = '张三'
money = 20.6
strformat = "%s今天消费%d" % (name, money)
strformat1 = "%s今天消费%f" % (name, money)
print(strformat)
print(strformat1)

# format 方法实现字符串格式化
hello__format = 'hello,{}'.format('world')
print(hello__format)

format1 = 'hello,{},{}'.format('world', 'python')
print(format1)

# 指定位置
format1 = 'hello,{0},{1},{0}'.format('world', 'python')
print(format1)

# 通过名字传参数
name__format = 'hello,{name1},{name2},{name1}'.format(name1='你好', name2='小红')
print(name__format)

# 对数字进行格式化,四舍五入
print('{:.2f}'.format(3.1635926))
print('{{{:.2f}}}'.format(3.1635926))

str = 'abcdefab'
# 返回首次匹配的索引，找不到返回-1
find = str.find('ab')
print(find)

print(str.rfind('ab'))

print(str.rindex('ab'))  # 从右边查找
# print(str.index('ac'))  # 找不到将报错

# 综上，find好

# count 子串出现的次数
print(str.count('a'))

# 替换
print(str.replace("a", 'A'))

# 字符串切分
split = str.split('d')
for s in split:
    print(s)
print(type(split))

# 把首字母大写,其后的小写
str = 'hello WWorld，你好'
print(str.capitalize())
# 每个单词首字母大写，其后的小写
print(str.title())
# 全部大写
print(str.upper())
# 全部小写
print(str.lower())

str0 = 'hello world'
print(str0.startswith('h'))
print(str0.endswith('h'))

print("======", str0.__eq__('hello world'))

str1 = '   he    lo   a         '
# 去除右边的空白字符
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())


# ========================练习==========================
# 字符串反转
str = 'hello world'
str3 = str[::1]  # 隔一个取一个
str1 = str[::-1]  # 反转字符串
print(str1)
print(len(str1))  # 获取字符串的长度
