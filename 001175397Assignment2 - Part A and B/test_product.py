import unittest
from checkoutRegister import CheckoutRegister, Product

class TestProduct(unittest.TestCase):
    def test_get_barcode(self):
        product = Product(123, "Milk, 2 Litres", "Fresh whole milk", 3.50)
        self.assertEqual(product.get_barcode(), 123)

    def test_get_name(self):
        product = Product(123, "Milk, 2 Litres", "Fresh whole milk", 3.50)
        self.assertEqual(product.get_name(), "Milk, 2 Litres")

    def test_get_description(self):
        product = Product(123, "Milk, 2 Litres", "Fresh whole milk", 3.50)
        self.assertEqual(product.get_description(), "Fresh whole milk")

    def test_get_price(self):
        product = Product(123, "Milk, 2 Litres", "Fresh whole milk", 3.50)
        self.assertEqual(product.get_price(), 3.50)

if __name__ == '__main__':
    unittest.main()
