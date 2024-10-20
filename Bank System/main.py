from BankAccounts import *

dev = BankAccount("Dave", 1000)
dev.deposit(500)

taylor = BankAccount("Taylor", 500)
dev.transfer(9000, taylor)

# Rewards on deposits
jim = InterestRewardsAcct("Jim", 500)
jim.deposit(100)
jim.transfer(100, dev)

# Penalized on Withdrawal
kate = SavingsAcct("Kate", 1000)
kate.transfer(100, jim)
kate.withdraw(600)
