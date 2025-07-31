class Person:
    __slots__ = ('name')
    def __init__(self, name):
        self.name = name


p  = Person("vishwas")
print(p.name)

print(p.__dict__)
p.email = "vishwas@cloudthat.com"
print(p.email)