import unittest
from vending_machine.vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def test_insert_money(self):
        vm = VendingMachine()
        self.assertEqual(vm.insert_money(100), 100)

    def test_deposit(self):
        vm = VendingMachine()
        vm.insert_money(100)
        self.assertEqual(vm.deposit(), 100)
        vm.insert_money(50)
        self.assertEqual(vm.deposit(), 150)

    def test_refund(self):
        vm = VendingMachine()
        vm.insert_money(200)
        vm.insert_money(100)
        self.assertEqual(vm.refund(), 300)
        self.assertEqual(vm.deposit(), 0)
