# coding=utf-8
import threading
import time
import random
from queue import Queue


class Producer(threading.Thread):

    def __init__(self, t_name, queue):
        threading.Thread.__init__(self,  name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("%s:%s is producing %d to the queue!"%(time.ctime(), self.getName(), i))
            self.data.put(i)
            time.sleep(random.randrange(10)/5)
        print("%s : %s producing finished!"%(time.ctime(), self.getName()))

class Consumer(threading.Thread):
    """
    consumer thread 消费线程
    """
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("%s : %s is consuming. %d in the queue is consumed!"%(time.ctime(), self.getName(), val))

            time.sleep(random.randrange(10))
        print("%s : %s consuming finished!"%(time.ctime(), self.getName()))

def main():
    """
    main thread 主线程
    :return:
    """
    queue = Queue()  #队列实例化
    producer = Producer("Pro", queue)
    consumer = Consumer("Con", queue)
    producer.start()  # 开始制造
    consumer.start()  # 开始消费
    """
    join()的作用是，在子线程完成运行之前，这个子线程的父线程将一直被组赛
    join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行
    """
    producer.join()
    consumer.join()
    print("All threads terminate")

if __name__ == '__main__':
    main()

