class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit):
        return self.balance + deposit
    
    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            return "OK"
        else:
            return "Your balance is less than withdraw."

owner = input()
balance = int(input())

bank = Account(owner, balance)

depos = int(input())
print(bank.deposit(depos))

withdr = int(input())
print(bank.withdraw(withdr))