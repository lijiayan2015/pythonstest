__author__ = 'lijiayan'

"""
语法:
class ClassName(parentClass):
    语句块
"""


class MyClass:
    # 类属性,可以用类名访问,也可以用其对象访问
    x = 'abc'

    # 初始化方法,在类对象创建的时候调用
    def __init__(self, name):
        self.info = "info"
        self.name = name

    """
    # 构造方法
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super(MyClass, cls).__new__(*args, **kwargs)
    """

    # self 相当于this,代表使用这个方法的对象
    # self 不推荐修改参数名
    def foo(self):
        print('myclass')
        print(self.__y)

    # 私有变量,可内部访问
    # 外部可用MyClass.dict查看重命名后的对象名进行访问
    __y = 'bcd'

    # get方法
    def getY(self):
        return MyClass.__y

    # 定义保护变量,只是一种约定,实质和普通变量一样的
    _z = "protect"

    # 定义静态方法
    @staticmethod
    def static_mythod():
        print("这是静态方法")

    # 定义类方法
    @classmethod
    def class_method(cls):
        print('class={{0,__name__,({0})}}'.format(cls))

# obj = MyClass
# print(MyClass.x, MyClass.foo(obj))
# obj.foo(obj)
# print(type(MyClass))
obj = MyClass("zhangsan")
obj.age = 20

obj1 = MyClass("lisi")
print(obj.info, obj.name, obj.age)
print(obj1.info, obj1.name)

print(MyClass.__dict__)
print(obj.__dict__)

# 调用get方法
print(obj.getY())
MyClass.static_mythod()
MyClass.class_method()
obj.class_method()
obj.static_mythod()