class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
    def deposite(self, amountoDeposit, password):
        if password != self.password:
            print("Incorrect password")
            return None
        if amountoDeposit < 0:
            print('Negative amount')
            return None
        else:
            self.balance += amountoDeposit
            return self.balance
    def withdraw(self, amunttoWithdrow, password):
        if password != self.password:
            print("Incorrect password")
            return None
        if amunttoWithdrow > self.deposite:
            print('It is more than what you have')
            return None
        if amunttoWithdrow > self.deposit:
            self.balance -= amunttoWithdrow
            return self.balance
    def GetBalance(self, password):
        if password != self.password:
            print("Incorrect password")
            return None
        return self.balance
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()
A = Account("Maria", 100000, "Brain")
A.deposite(150000, "Brain")
A.GetBalance("Brain")
A.show()
        
           
