# coding=utf-8

class A(object):

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


b = A(name="jack")
print(hasattr(b, "name"))
print(setattr(b, "name", 123))
setattr(b, "age", 222)
print(b.name)
print(hasattr(b, "age"))
print(getattr(b, "age"))
print(hasattr(b, "print_name"))