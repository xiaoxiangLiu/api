# coding=utf-8
import unittest

class Demo(object):

    def __init__(self):
        self._name = "jack"

    @property
    def name(self):
        return self._name

d = Demo()
print(d.name)