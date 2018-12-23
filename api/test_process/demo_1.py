# coding=utf-8
from queue import Queue

q = Queue()  # 接受参数maxsize，最大容量
q.put()
q.put("yang")
q.put(4)
q.put([1,2,3])
print("q.qsize()：", q.qsize())  # 返回队列大小
print("q.empty()：", q.empty())  # 如果为空返回True，如果不为空返回False
print("q.full()：", q.full())  # 如果满了返回True，如果不满返回False
print(q.get())
print(q.get())
print(q.get())