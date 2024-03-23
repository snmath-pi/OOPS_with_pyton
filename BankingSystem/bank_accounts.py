class BalanceException(Exception):
    pass    

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance= ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
    def deposit(self, amt):
        self.balance += amt
        print("Deposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amt):
        if self.balance >= amt:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}"
            )
            
    def withdraw(self, amt):
        try:
            self.viableTransaction(amt)
            self.balance -= amt
            print('\nWithdraw complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    def transfer(self, amt, acct):
        try:
            print('\n**********\n\nBeginning Transfer...🤑🚀')
            self.viableTransaction(amt)
            self.withdraw(amt)
            acct.deposit(amt)
            print('\nTransfer complete! ✅\n\n*********')
        except BalanceException as error:
            print(f"\nTransfer interrrupted. ❌ {error}")
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amt):
        self.balance  = self.balance + (amt * 1.05)
        print("\nDeposit complete.")
        self.getBalance()
        
class SavingsAcct(InterestRewardsAcct):
    def __int__(self, initialamt, acct):
        super().__init__(initialamt, acct)
        self.fee = 5
    def withdraw(self, amt):
        try:
            self.viableTransaction(amt + 5)
            self.balance = self.balance - (amt + 5)
            print('\nWithdraw complete.')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')