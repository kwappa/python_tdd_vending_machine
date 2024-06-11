import unittest
from vending_machine.vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def test_insert_money(self):
        vm = VendingMachine()
        self.assertEqual(vm.insert_money(100), 100)
