class BankAccount:
    __model = "210-"
    __account_quantity = 0

    def __init__(self):
        self.__balance = 0
        self.__owner = ""
        self.__number = BankAccount.__model + \
                        str(BankAccount.__account_quantity)
        BankAccount.__account_quantity += 1

    def set_owner(self, owner):
        self.__owner = owner

    def get_number(self):
        return self.__number

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return "le solde du compte: " + self.__number + \
               " est de: " + str(self.__balance)


