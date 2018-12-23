# coding=utf-8
import threading
from BeautifulReport import BeautifulReport
import unittest
import time
import ddt
import queue


class MyThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            tests = self.queue.get()
            result = BeautifulReport(tests)
            result.report(description="测试报告", log_path="/", filename="自动化测试报告")
            self.queue.task_done()

def go():
    q = queue.Queue()
    tests = unittest.defaultTestLoader.discover(start_dir="./", pattern="test*.py")
    for i in tests:
        print(i)
        q.put(i)

    # 开启多线程
    transtion_id_list= [1,2,3,4,5,6,7]
    for i in transtion_id_list:
        t = threading.Thread(target=q, args=(i,))
        t.setDaemon(True)
        t.start()

    q.join()

if __name__ == '__main__':
    go()


