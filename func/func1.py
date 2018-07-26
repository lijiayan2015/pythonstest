__author__ = 'lijiayan'
"""
函数,其实就是一个代码块
函数定义的语法:
def funName(args):
    body
    [return]
"""


# 无参数函数
def fun1():
    print("this is my first python funuc")


# 定义有参数函数
def fun2(x, y):
    return x + y


# 定义一个无惨空方法
def fun3():
    pass


# 默认值参数的方法
def fun4(name, age=20, sex='男'):
    print("name:" + name + " age:" + str(age) + " sex:" + sex)


# 可变参数
# 位置参数的可变,nums是元组类型
# 该方式不能通过关键字传参
def add(*nums):
    sum = 0
    for x in nums:
        sum += x
    print(sum)


# 关键字参数可变参数
def build_profile(name, gender, **user_info):
    profile = {'name': name, 'gender': gender}
    print(type(user_info))
    for k, v in user_info.items():
        profile[k] = v
    print(profile)


import math


# 返回多个值
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.cos(angle)
    return nx, ny  # 返回结果最后的元组类型


# 程序的入口方法
# 如果当前模块作为其他模块的导入,则该方法不执行
if __name__ == '__main__':
    fun1()
    print("计算的结果是:%d" % fun2(y=80, x=30))
    fun4("张三", sex="女", age=18)
    add(1, 2, 3, 5)
    build_profile('张三', 'male', country='China', city='bj')
    build_profile(country='China', city='bj', name='张三', gender='male')
    res = move(1, 2, 5, 50)
    print(res[0], res[1])
