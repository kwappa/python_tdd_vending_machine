class VendingMachine:
    def __init__(self):
        self._deposit = 0
        pass

    def insert_money(self, money):
        self._deposit += money
        return money

    def deposit(self):
        return self._deposit
