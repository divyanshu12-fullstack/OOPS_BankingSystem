class BalanceException(Exception):
    pass


# Making Custom Errors


class BankAccount:
    def __init__(self, name, initial_amount):
        self.name = name
        self.balance = initial_amount
        print(f"\nAccount created for {name}. Initial Balance is: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Account '{self.name}' balance = ${self.balance}")

    def deposit(self, credit):
        self.balance += credit
        print("\nDeposit Complete")
        self.get_balance()

    def valid_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, Account {self.name} only"
                                   f" has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.valid_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    # Passing Object as argument, here account is the object
    def transfer(self, transfer_value, account):
        try:
            print("\n**********"
                  "\n\nBeginning Transfer....🚀")
            self.valid_transaction(transfer_value)
            self.withdraw(transfer_value)
            account.deposit(transfer_value)
            print("\nTransfer Complete! "
                  "\n\n********** ✅")
        except BalanceException as error:
            print(f"\nTransfer interrupted: {error}❌")


# Inheritance by below class
class InterestRewardsAcct(BankAccount):
    def deposit(self, credit):
        self.balance = self.balance + (credit * 1.05)
        print("Deposit complete")
        self.get_balance()


# Super used when you want to extend functionality of parent
# Super automatically calls parent's constructor
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, acct_name, initial_balance):
        super().__init__(acct_name, initial_balance)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.valid_transaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw Complete")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")
