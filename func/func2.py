__author__ = 'lijiayan'
"""
高阶函数:
参数或者返回值是函数
"""
f = abs
print(f(-1))


# 参数是函数
def add(a, b, f):
    return f(a) + f(b)


print(add(-3, -5, f))


# 返回值是函数
def lazy_sum(*nums):
    def sum():
        res = 0
        for x in nums:
            res += x
        return res

    return sum


ff = lazy_sum(12, 14)
print(ff())
