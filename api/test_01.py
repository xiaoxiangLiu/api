# coding=utf-8
import unittest
from logger import logger
import time
import threading
import pytest
from unittest.case import SkipTest

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_01(self):
        for i in range(3):
            with self.subTest():
                print(threading.currentThread)
                logger.info(u"test_01----01  start")
                time.sleep(2)
                logger.info(u"test_01____01 end")
                self.assertEqual(i, 2)

    def test_02(self):
        print(threading.currentThread)
        logger.info("test_01----02 start")
        time.sleep(1)
        logger.info("test_01------02  end")


if __name__ == '__main__':
    unittest.main()
