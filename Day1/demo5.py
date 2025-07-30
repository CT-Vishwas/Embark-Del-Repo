#!/usr/bin/env python3
# Script demo of class decorator which adds attribute to a class

def add_attribute(cls):
    cls.MY_ATTRIBUTE = 5
    return cls

@add_attribute
class MyClass:
    def __init__(self, value):
        self.value = value


obj = MyClass(10)
print(obj.value)
print(obj.MY_ATTRIBUTE)