class Account:
    def __init__(self, balance, acNumber):
        self.balance = balance
        self.acNumber = acNumber


    def debit(self, amount):
        self.balance = self.balance - amount
        print("Debit Successfull \nNew Balance: ",self.balance)

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Credit Successfull \nNew Balance: ",self.balance)



u1 = Account(1000, 1)
u2 = Account(5000, 2)
print(u1.balance)
u1.credit(1200)
u1.debit(200)
print(u1.balance)