from link.Node import Node


"""
单链表类
"""


class SingleLink(object):
    def __init__(self, node):
        self.__head = node

    # 判断链表是否为空
    def is_empty(self):
        return self.__head is None

    # 获取链表的长度
    def length(self):
        count = 0
        cur = self.__head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 遍历链表
    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    # 往头部添加元素
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    # 往链表的尾部添加一个元素
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            # 将当前游标移动到链表的尾部
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 在任意位置插入一个元素
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)

        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    # 移除一个元素
    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    # 查找一个元素
    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
