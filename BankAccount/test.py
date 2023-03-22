from account import BankAccount

account = BankAccount("123456789", "savings", 1000)

account.deposit(500)

account.withdraw(200)

print("Account balance:", account.get_balance())
