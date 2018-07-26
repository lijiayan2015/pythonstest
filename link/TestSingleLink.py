from link.Node import Node
from link.SingleLink import SingleLink

node = Node(5)
singleLink = SingleLink(node)
print(singleLink.is_empty())
singleLink.add(3)
singleLink.append(10)
singleLink.travel()
singleLink.insert(2,20)
print("=============")
singleLink.travel()
singleLink.remove(3)
print("==========")
singleLink.travel()
