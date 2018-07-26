__author__ = 'lijiayan'


class Node(object):
    """
    树的节点
    """

    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None
