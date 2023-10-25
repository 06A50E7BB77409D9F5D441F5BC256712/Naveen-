'''Implement a class called BankAccount that represents a bank account. The class should have private
attributes for account number, account holder name, and account balance. Include methods to
deposit money, withdraw money, and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the class. Write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionality.'''

class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self._account_number = account_number
      self._account_holder_name = account_holder_name
      self._account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self._account_balance += amount
          return f"Deposited ${amount}. New balance: ${self._account_balance}"
      else:
          return "Invalid deposit amount"

  def withdraw(self, amount):
      if 0 < amount <= self._account_balance:
          self._account_balance -= amount
          return f"Withdrew ${amount}. New balance: ${self._account_balance}"
      else:
          return "Invalid withdrawal amount"

  def display_balance(self):
      return f"Account Balance for {self._account_holder_name} ({self._account_number}): ${self._account_balance}"

# Test the BankAccount class
if __name__ == "__main__":
  # Create a BankAccount instance
  account = BankAccount("123456", "leo das", 1000.0)

  # Deposit money
  print(account.deposit(500))
  print(account.display_balance())

  # Withdraw money
  print(account.withdraw(200))
  print(account.display_balance())

  # Attempt to withdraw an invalid amount
  print(account.withdraw(1500))  # Should print "Invalid withdrawal amount"





