# create a class bank account
# it has 2 fields: name and balance
# it has methods to withdraw and deposit and print statement


class Account(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def print_statement(self):
        print(str(self.name) + ": " + str(self.balance) + "€")


myaccount = Account(1000, "Sari")

myaccount.print_statement()
myaccount.deposit(500)
myaccount.print_statement()
myaccount.withdraw(100)
myaccount.print_statement()