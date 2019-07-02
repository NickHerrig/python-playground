
class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: {self.balance}'

    def deposit(self, ammount):
        """
        This method allows a numeric deposit of money.

        Parameters:
        ammount (int or float): ammount of deposit

        Returns:
        str: 'Deposit Accepted'
        """
        self.balance += ammount
        return 'Deposit Accepted'

    def withdraw(self, ammount):
        if self.balance >= ammount:
            self.balance -= ammount
            return 'Withdraw Accepted'
        return 'Funds Unavailable'
