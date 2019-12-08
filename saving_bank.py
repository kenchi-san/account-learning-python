from compte_bank import *


class SavingsAccount(BankAccount):
    __minimum_balance = 0
    __interest = 0.1

    def compute_interest(self):
        self.deposit(self.get_balance() * SavingsAccount.__interest)

    def withdraw(self, amount):
        if (self.get_balance() - amount) >= \
                SavingsAccount.__minimum_balance:
            BankAccount.withdraw(self, amount)
        else:
            print("Pas assez d'argent sur le compte")
