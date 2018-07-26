from stack.Stack import Stack

__author__ = 'lijiayan'

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    for i in range(s.size()):
        print(s.pop())

    print("栈大小：" + str(s.size()))
