from account import Account

my_account = Account('Randy')
your_account = Account('Boob')
your_account.deposit(5)
my_account.deposit(100)
print (my_account.balance)
print(my_account.withdraw(150))
#print(my_account.balance)
print(my_account)
print(your_account)
print(your_account<=my_account)
