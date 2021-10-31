import unittest
from unittest import result
from items import add, displayCatalog, addItem, main, viewCart, viewOrder

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = main()
    # The catalog has to have 7 or more items
    def test_catalog(self):
        result = displayCatalog()
        self.assertGreater(result, 7, "Success")
    
    def test_cart(self):
        result = viewCart()
        self.assertGreater(result, 0, "No items in the cart")

    def test_order(self):
        result = viewOrder()
        self.assertGreater(result, 0, "No items in the order")
        
    def test_add(self):
        result = add(10,5)
        self.assertEqual(result, 15)

    def test_addItem(self):
        result = addItem(4)
        self.assertGreaterEqual(result, 4, 6)


if __name__ == '__main__':
    unittest.main()

