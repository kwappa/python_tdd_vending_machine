class VendingMachine:
    ACCEPTABLE_MONEYS = (10, 50, 100, 500, 1000)

    def __init__(self):
        self._deposit = 0
        self._sales_amount = 0
        self._beverages = [
            {"name": "cola", "price": 120, "count": 5},
        ]

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

    def add_beverage(self, beverage):
        self._beverages.append(beverage)

    def beverages(self):
        return self._beverages

    def is_buyable(self, beverage_name):
        for beverage in self._beverages:
            if beverage_name == beverage["name"]:
                return (self._deposit >= beverage["price"]) & (beverage["count"] > 0)
        return False

    def buy(self, beverage_name):
        if self.is_buyable(beverage_name):
            for beverage in self._beverages:
                if beverage["name"] == beverage_name:
                    beverage["count"] -= 1
                    self._deposit -= beverage["price"]
                    self._sales_amount += beverage["price"]
                    return beverage_name
        return None

    def sales_amount(self):
        return self._sales_amount

    def buyable_beverages(self):
        return [beverage["name"] for beverage in self._beverages if self.is_buyable(beverage["name"])]
