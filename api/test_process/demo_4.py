# coding=utf-8
from multiprocessing import Process, Queue
import os,time,random

# 写入数据进程执行的代码
def write(q):
    for value in ["A", "B", "C"]:
        print("Put %s to queue....gid：%s"%(value,os.getpid()))
        q.put(value)
        time.sleep(random.random())

# 读取数据执行的代码
def read(q):
    while not q.empty():
        value = q.get(True)
        print("Get %s from queue..gid：%s"%(value,os.getpid()))
        time.sleep(random.random())

if __name__ == '__main__':  # 如果使用进程池则需要使用multiprocessing.Manager()
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入
    pw.start()
    # 等待pw结束：
    pw.join()
    # 启动子进程pr，读取：
    pr.start()
    pr.join()
    print("所有数据都写入并且读完")
