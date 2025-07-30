#!/usr/bin/env python3
# Advanced OOPs Concepts

class BankAccount:
    def __init__(self, owner, balance, account_number):
        self.owner = owner # This is a Public attribute
        self._balance = balance # Protected
        self.__account_number = account_number # private attribute ( name Mangling)
    
    @property
    def balance(self):   # Getter
        return self._balance
    
    @balance.setter
    def balance(self, amount): # setter
        calculated_balance = self._balance + amount
        if calculated_balance < 0:
            print("Less than minimum balance")
        else:
            self._balance = calculated_balance

    @property
    def account_number(self):
        return f"***{self.__account_number[-3:]}"
    
class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        self._balance += self._balance * rate

# account = BankAccount("vishwas", 1000, "12345678")
account = SavingsAccount("vishwas", 1000, "12345678")

print(account.owner)
#print(account._balance) # But not recommended
# print(account.__account_number)
#print(account._BankAccount__account_number) # not recommended

print(f"Accessing the account with account number: {account.account_number}")
# Access the balance
print(account.balance)

# Credit the amount
account.balance = 1000

# Check the balance
print(f"Amount credited. Remaining Balance: {account.balance}")

# Debit the amount
account.balance = -500

# Check the balance 
print(f"Amount debited. Remaining Balance: {account.balance}")

# Apply interest Rate
account.apply_interest(0.02)

print(f"Accout balance after interest credit. {account.balance}")