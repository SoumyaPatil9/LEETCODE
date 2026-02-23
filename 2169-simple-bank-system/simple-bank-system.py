class Bank:

    def __init__(self, balance):
        # Store balances
        self.balance = balance
        self.n = len(balance)

    def is_valid(self, account):
        # Check if account number is between 1 and n
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        # Check valid accounts
        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        
        # Check sufficient balance
        if self.balance[account1 - 1] < money:
            return False
        
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        # Check valid account
        if not self.is_valid(account):
            return False
        
        # Deposit money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        # Check valid account
        if not self.is_valid(account):
            return False
        
        # Check sufficient balance
        if self.balance[account - 1] < money:
            return False
        
        # Withdraw money
        self.balance[account - 1] -= money
        return True


# Example usage:
bank = Bank([10, 100, 20, 50, 30])

print(bank.withdraw(3, 10))     # True
print(bank.transfer(5, 1, 20))  # True
print(bank.deposit(5, 20))      # True
print(bank.transfer(3, 4, 15))  # False
print(bank.withdraw(10, 50))    # False