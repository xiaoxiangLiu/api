# coding=utf-8
from selenium import webdriver



class Base(object):

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        return self.driver.get(self.url)

    def find_element(self, *loc):
        self.driver.find_element(*loc)

