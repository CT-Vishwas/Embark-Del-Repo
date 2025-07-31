class FactoryMeta(type):
    def __new__(cls,name,bases,attrs):

        def from_dict(cls,data):
            return cls(**data)
        
        attrs['from_dict'] = classmethod(from_dict)
        print(f"Adding a factory method to: {name}")
        return super().__new__(cls,name,bases,attrs)


class BankAccount(metaclass=FactoryMeta):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance




acc_data = {"owner":"Vishwas","balance":1000}
acc = BankAccount.from_dict(acc_data)


print(acc.owner, acc.balance)