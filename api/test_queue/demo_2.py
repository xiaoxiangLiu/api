# coding=utf-8
from queue import LifoQueue

q = LifoQueue()  # Fifo 即先进后出，与栈类似

for i in range(5):
    q.put(i)

while not q.empty():  # 当队列不位空时，取出数据
    print(q.get())


