__author__ = 'lijiayan'


class Queue(object):
    """
    队列
    """

    def __init__(self):
        self.__list = []

    # 入队
    def enqueue(self, item):
        # 从尾部添加元素
        self.__list.append(item)

    # 出对操作
    def dequeue(self):
        # 从队列头部删除元素
        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

    def size(self):
        return len(self.__list)
