class BankAccount():
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    def display_balance(self):
        return f"Balance: {self.balance}"

account = BankAccount('Akash')
account.deposit(1000)
account.withdraw(500)
print(account.display_balance())