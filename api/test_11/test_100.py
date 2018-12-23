# coding=utf-8
import unittest
import time
from logger import logger



class TestCase(unittest.TestCase):

    def test_01(self, num):
        print(time.ctime())
        time.sleep(1)
        print(num)
        logger.info("test_100------test_01---%s"%num)
        print("i am test_01----------transtion_id:  %s")

    def test_02(self):
        print(time.ctime())
        time.sleep(1)
        logger.info("test_100-----test_02transtion_id:::%s")
        print("i am test_02")

if __name__ == '__main__':
    TestCase().test_01(num=1)