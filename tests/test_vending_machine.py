import unittest
from vending_machine.vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()

    def test_insert_money(self):
        self.assertEqual(self.vm.insert_money(100), 100)

    def test_deposit(self):
        self.vm.insert_money(100)
        self.assertEqual(self.vm.deposit(), 100)
        self.vm.insert_money(50)
        self.assertEqual(self.vm.deposit(), 150)

    def test_refund(self):
        self.vm.insert_money(500)
        self.vm.insert_money(100)
        self.assertEqual(self.vm.refund(), 600)
        self.assertEqual(self.vm.deposit(), 0)

    def test_acceptable_money(self):
        self.vm.insert_money(100)
        self.assertEqual(self.vm.deposit(), 100)
        self.assertEqual(self.vm.insert_money(55), 55)
        self.assertEqual(self.vm.deposit(), 100)

    def test_initial_beverages(self):
        self.assertTrue({"name": "cola", "price": 120, "count": 5} in self.vm.beverages())

    def test_is_buyable(self):
        self.assertFalse(self.vm.is_buyable("cola"))
        self.vm.insert_money(500)
        self.assertTrue(self.vm.is_buyable("cola"))

    def test_buy_cola(self):
        self.vm.insert_money(500)
        self.assertEqual(self.vm.buy("cola"), "cola")
        self.assertEqual(self.vm.deposit(), 380)
        self.assertTrue({"name": "cola", "price": 120, "count": 4} in self.vm.beverages())

        # cannot buy because of luck of deposit
        for _ in range(3): self.vm.buy("cola")
        self.assertEqual(self.vm.deposit(), 20)
        self.assertIsNone(self.vm.buy("cola"))

        # cannot buy because of luck of stock
        self.vm.insert_money(500)
        self.assertTrue(self.vm.buy("cola"), "cola")
        self.assertEqual(self.vm.deposit(), 400)
        self.assertIsNone(self.vm.buy("cola"))

    def test_sales_amount(self):
        self.assertEqual(self.vm.sales_amount(), 0)
        self.vm.insert_money(500)
        self.vm.buy("cola")
        self.assertEqual(self.vm.sales_amount(), 120)
        self.vm.buy("cola")
        self.assertEqual(self.vm.sales_amount(), 240)
        self.assertEqual(self.vm.refund(), 260)

    def test_add_beverage(self):
        self.vm.add_beverage({"name": "water",   "price": 100, "count": 5})
        self.vm.add_beverage({"name": "redbull", "price": 200, "count": 5})
        self.assertTrue({"name": "water",   "price": 100, "count": 5} in self.vm.beverages())
        self.assertTrue({"name": "redbull", "price": 200, "count": 5} in self.vm.beverages())
        self.assertTrue({"name": "cola",    "price": 120, "count": 5} in self.vm.beverages())

    def test_buyable_beverages(self):
        self.vm.add_beverage({"name": "water",   "price": 100, "count": 5})
        self.vm.add_beverage({"name": "redbull", "price": 200, "count": 5})
        # nothing can buy before insert money
        self.assertTrue(not any(beverage["name"] in self.vm.buyable_beverages() for beverage in self.vm.beverages()))
