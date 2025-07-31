class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['custom_attribute'] = 'This is a custom attribute'
        return super().__new__(cls,name, bases, attrs)
    

class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value


obj = MyClass(10)

print(obj.value)
print(obj.custom_attribute)