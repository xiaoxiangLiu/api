# coding=utf-8
from collections import namedtuple

str_list = [
    ("a", "aaa.com", "aaaaa.com"),
    ("b", "bbb.com", "bbbbb.com"),
    ("c", "ccc.com", "ccccc.com"),
]

name = namedtuple("type", ("base_url", "mysql_type", "redis_type"))

for na in str_list:
    named = name._make(na)
    print(named.base_url)
    print(named.mysql_type)
    print(named.redis_type)