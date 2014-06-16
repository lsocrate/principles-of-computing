def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for x in range(25):
        lst.append(sum(lst[-3:]))
    return lst

class BankAccount:
    fee = 5

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        if self.balance - amount < 0:
            self.fees += self.fee
            self.balance -= self.fee
        self.balance -= amount

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees
