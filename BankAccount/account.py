class BankAccount:
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("There is no enough money")
    def get_balance(self):
        return self.balance
    
    