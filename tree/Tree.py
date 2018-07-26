from tree.Node import Node

__author__ = 'lijiayan'


class Tree(object):
    """
    二叉树
    """

    def __init__(self):
        self.root = None

    # 添加节点
    def add(self, item):
        node = Node(item)

        # 判断root节点是不是null
        if self.root is None:
            self.root = node
            return
        # 如果不是空树
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            # 检查左子树是不是kong，如果空，可以插入当前节点
            if cur.lchild is None:
                cur.lchild = node
                return
            else:
                queue.append(cur.lchild)

            if cur.rchild is None:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)

    # 遍历二叉树之广度优先遍历
    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur = queue.pop(0)
            print(cur.item)
            # 判断当前访问的节点有没有左右孩子
            # 有的话，入队
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)

    # 深度优先遍历之先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.item)
        self.preOrder(node.lchild)
        self.preOrder(node.rchild)
