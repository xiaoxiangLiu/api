# coding=utf-8
from collections import OrderedDict


demo_dict = {
    "a":1,
    "b":2,
    "c":3,
}
Order_dict = OrderedDict(demo_dict)
for i, v in Order_dict.items():
    print(i, v)