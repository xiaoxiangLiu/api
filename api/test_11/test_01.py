# coding=utf-8
import unittest
import requests
import time
from logger import logger

class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        print(time.ctime())
        url = "https://www.baidu.com"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        }

        s = requests.session()
        resp = s.get(url, headers=headers)
        s.close()
        logger.info("test_01-----01::::访问状态：{0}".format(resp.status_code))
        print(resp.status_code)

if __name__ == '__main__':
    unittest.main()
