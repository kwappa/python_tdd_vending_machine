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
        self.vm.insert_money(200)
        self.vm.insert_money(100)
        self.assertEqual(self.vm.refund(), 300)
        self.assertEqual(self.vm.deposit(), 0)
