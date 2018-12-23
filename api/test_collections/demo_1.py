# coding=utf-8
from collections import Counter

a = "aksjdkajsdkjad"
b = Counter(a)
print(b.most_common()[:-3:-1])



