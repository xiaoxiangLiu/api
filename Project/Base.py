# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



class Base(object):

    """
    基础类
    """

    def __init__(self, driver='chrome'):

        """
        构造
        :param driver:选择浏览器驱动，默认谷歌
        :return:
        """

        if driver == 'chrome' or driver == 'Chrome':
            self.driver = webdriver.Chrome()
        elif driver == 'ff' or driver == 'firefox' or driver == 'Firefox':
            self.driver = webdriver.Firefox()
        elif driver == 'ie' or driver == 'Ie':
            self.driver = webdriver.Ie()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open(self, url='https://www.baidu.com'):
        """
        输入url
        :param url:
        :return:
        """
        self.driver.get(url)

    def get_element(self, *loc):
        """
        获取页面元素
        :param loc:定位元素
        :return:
        """
        return self.driver.find_element(*loc)

    def get_elements(self, *loc) -> list:

        """
        获取一组页面元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*loc)

    def left_click(self, *loc):

        """
        左键点击
        :return:
        """
        self.get_element(*loc).click()

    def right_click(self, *loc):
        """
        右键点击
        :param loc:
        :return:
        """
        element = self.get_element(*loc)
        ActionChains(self.driver).context_click(element).perform()

    def double_click(self, *loc):
        """
        左键双击
        :return:
        """
        element = self.get_element(*loc)
        ActionChains(self.driver).double_click(element).perform()

    def send_data(self, data, *loc):
        """
        输入数据
        :param loc:
        :return:
        """
        self.get_element(*loc).send_keys(data)

    def