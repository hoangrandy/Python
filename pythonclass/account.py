class Account(object):
    """
    Represent a bank account.

    Argument:
    account_holder(string): account holder's name.

    Attributes:
    holder(string):account holder's name.
    balance(float): account balance in dollars
    """

    def __init__(self, account_holder, balance = 0):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """
        deposit amount to the account
        Parameter:
        amount(float): the amount to be deposited in dollars.
        Returns:
        the updated account object
        """
        self.balance+= amount
        return self

    def withdraw(self, amount):
        """
        withdraw an amount from the account
        Parameter:
        amount(float): the amount to be withdrawn from the account_holder
        Returns:
        the updated account object otherwise false if amount withdrawn > acc
        """
        if amount < self.balance:
            self.balance -= amount
            return True
        else:
            print("You can not withdraw more than your balance")
            return False

    def __str__(self):
        # Let's return the account holder name and the amount they have
        return f'{self.holder}, Account Balance:{self.balance}'
