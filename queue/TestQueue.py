from queue import Queue

__author__ = 'lijiayan'

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    for i in range(queue.size()):
        print(queue.dequeue())
    print("size:" + queue.size())
