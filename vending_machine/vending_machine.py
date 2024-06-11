class VendingMachine:
    def __init__(self):
        self._deposit = 0
        pass

    def insert_money(self, money):
        if money == 55:
            return money
        self._deposit += money
        return money

    def deposit(self):
        return self._deposit

    def refund(self):
        deposit = self._deposit
        self._deposit = 0
        return deposit
