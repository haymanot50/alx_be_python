# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Deposit a given amount."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw a given amount if funds are sufficient."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance in the required format (2 decimal places)."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
