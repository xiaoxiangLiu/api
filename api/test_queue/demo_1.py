# coding=utf-8
from queue import Queue

q = Queue()  # 默认是FIFO队列，即先进先出

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())


