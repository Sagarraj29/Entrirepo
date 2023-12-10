class BankAccount:
    def __init__(self, login_name, pin, balance=0):
        self.login_name = login_name
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return self.pin == entered_pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds. Withdrawal not allowed.")
#my account
account1 = BankAccount(login_name='sagar_raj', pin='1234', balance=10000)

# Account login details
entered_login_name = input("welcome to abc bank\nEnter your login name: ")
entered_pin = input("Enter your PIN: ")

if account1.login(entered_pin) and entered_login_name == account1.login_name:
    print("Login successful!\n")

    # Deposit
    deposit_amount = float(input("Enter the deposit amount: "))
    account1.deposit(deposit_amount)

    # Withdrawal
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    account1.withdraw(withdrawal_amount)

else:
    print("Login failed. Invalid login name or PIN.")
