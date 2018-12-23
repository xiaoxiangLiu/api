# coding=utf-8
import unittest
from logger import logger
import time

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        import threading
        print(threading.currentThread)
        logger.info(u"test_02-----01  start")
        time.sleep(3)
        logger.info(u"test_02------01  end")
