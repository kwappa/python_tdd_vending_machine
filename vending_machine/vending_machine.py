class VendingMachine:
    ACCEPTABLE_MONEYS = (10, 50, 100, 500, 1000)

    def __init__(self):
        self._deposit = 0
        pass

    def insert_money(self, money):
        if money not in self.ACCEPTABLE_MONEYS:
            return money
        self._deposit += money
        return money

    def deposit(self):
        return self._deposit

    def refund(self):
        deposit = self._deposit
        self._deposit = 0
        return deposit
