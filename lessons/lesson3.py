class BankAccount:
    def __init__(self, account_no):
        self._account_no = account_no   # protected — номер счёта
        self.__balance = 0              # private — баланс; меняем только через deposit/withdraw
        self.__balance = 0             # private — баланс; меняем только через deposit/withdraw
        self.real_balance = 0

    def deposit(self, amount):
        if amount <= 0:
@@ -20,6 +21,24 @@ def withdraw(self, amount):
    def get_balance(self):
        return self.__balance

    # сеттер - установить значение приватного атрибута
    def set_balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance must be positive")
        self.__balance = new_balance

    @property
    def balance(self):
        # геттер
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        # сеттер
        if new_balance < 0:
            raise ValueError("Balance must be positive")
        self.__balance = new_balance

igor_account = BankAccount("igor")
print(igor_account._account_no)         # protected: прочитать снаружи можно (но не принято)
igor_account._account_no = "arseniy"    # protected: и поменять можно — это лишь договорённость
@@ -30,3 +49,10 @@ def get_balance(self):
igor_account.deposit(5000)              # нормальная сумма — баланс увеличится
# igor_account.deposit(-10000)          # бросил бы ValueError: сумма должна быть положительной
print(igor_account.get_balance())
igor_account.set_balance(3000)
print(igor_account.get_balance())

igor_account.real_balance = -1000000
print(igor_account.balance)
# igor_account.balance = -3500 # ошибка ValueError
print(igor_account.get_balance())