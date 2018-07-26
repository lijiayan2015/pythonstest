from tree.Tree import Tree

__author__ = 'lijiayan'

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)

    tree.breadth_travel()
    print("===========")
    tree.preOrder(tree.root)
