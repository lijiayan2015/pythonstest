__author__ = 'lijiayan'


class Stack(object):
    """
    栈
    """

    def __init__(self):
        self.__list = []

    # 入栈
    def push(self, item):
        self.__list.append(item)

    # 出栈
    def pop(self):
        return self.__list.pop()

    # 返回栈定的元素，并不会弹出栈
    def peek(self):
        if len(self.__list) > 0:
            return self.__list[-1]
        else:
            return None

    def if_empth(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)
