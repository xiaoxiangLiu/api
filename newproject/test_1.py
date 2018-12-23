# coding=utf-8
import pytest
import pytest_rerunfailures
from common import MyTest
from PO import HomePage


class TestCase(MyTest):
    """
    百度首页搜索测试
    """

    def test_01(self):
        """
        输入selenium，点击搜索
        :return:
        """
        HomePage(self.driver).search_selenium()
        print("test_01")
        assert False

    def test_02(self):

        HomePage(self.driver).search_selenium()
        print("test_02")
        assert True

if __name__ == '__main__':
    pytest.main("--reruns 1")
