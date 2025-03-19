class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}ETB. New balance: {self.__balance}ETB")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}ETB. New balance: {self.__balance}ETB")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdraw amount must be positive.")

    def get_balance(self):
        return f"Your current balance is: {self.__balance}ETB"
account = BankAccount(3000.00)
account.deposit(1200.00)
account.withdraw(1800.00)
print(account.get_balance())
