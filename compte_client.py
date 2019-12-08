from compte_bank import *
from saving_bank import *


class Client(BankAccount):

    def __init__(self, name, first_name, address, age):
        self.__name = name
        self.__first_name = first_name
        self.__age = age
        self.__address = address
        self.__my_accounts = []

    def get_name(self):
        return self.__name

    def get_adresse(self):
        return self.__address

    def move_out(self, new_address):
        self.__address = new_address

    def get_age(self):
        return "age: " + str(self.__age)

    def get_old(self):
        self.__age += 1

    def __str__(self):
        return "client : " + self.__first_name + \
               " " + self.__name

    def add_account(self, new_account):
        self.__my_accounts.append(new_account)
        new_account.set_owner(self)

    def identify_account(self):
        print(" sur quel compte ?")
        res = None
        x = input("?")

        for c in self.__my_accounts:
            if c.get_number() == x:
                res = c
                break
        return res

    def withdraw(self):
        c = self.identify_account()
        print("Quel montant ?")
        x = int(input("?"))
        c.withdraw(x)

    def deposit(self):
        c = self.identify_account()
        print("Quel montant ?")
        x = int(input("?"))
        c.deposit(x)


client1 = Client("hugo", "charon", "rue louise", 20)
Saving = SavingsAccount()
account1 = Saving

print(account1)

client1.add_account(account1)
client1.deposit()
print(account1)
client1.withdraw()
