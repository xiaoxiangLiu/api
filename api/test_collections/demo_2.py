# coding=utf-8
from collections import namedtuple

name = namedtuple("demo", ("x", "y"))
na = name(10,20)
print(na.x, na.y)
c = name._make([200, 300])
print(c.y, c.x)
c = c._replace(x = 10000)
print(c.x, c.y)
