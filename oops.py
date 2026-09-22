class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.transactions.append(f"Deposited: ₹{amount}")
            print("Money deposited:", amount)
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            self.transactions.append(f"Withdrawn: ₹{amount}" )
            print("Money withdrawn:", amount)

    # Show account details
    def show_balance(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: ₹", self.balance)

    # Show transaction history
    def show_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

class SavingsAccount(BankAccount):
    def show_account_type(self):
        print("Account Type: Savings Account")


# Create object
account = SavingsAccount("Rahul",101,10000)

# Account details
account.show_balance()
print()

account.deposit(2000)
print()

account.withdraw(3000)
print()

# Invalid withdrawal
account.withdraw(15000)
print()

# Account type
account.show_account_type()
print()

account.show_balance()

# Transaction history
account.show_transactions()
