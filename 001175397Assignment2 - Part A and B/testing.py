import unittest
from checkoutRegister import CheckoutRegister, Product

class TestCheckoutRegister(unittest.TestCase):
    def setUp(self):
        # Create an instance of CheckoutRegister for testing
        self.checkout_register = CheckoutRegister()

    def test_scan_item_product_found(self):
        # Add products to the CheckoutRegister
        self.checkout_register._products.append(Product(123, "Milk, 2 Litres", "Fresh whole milk", 3.50))
        self.checkout_register._products.append(Product(456, "Bread, 500g", "Soft white bread", 2.50))

        # Scan the first product (Milk, 2 Litres)
        self.checkout_register.scan_item(123)

        # Check if the total amount due is updated correctly
        self.assertEqual(self.checkout_register._total_amount_due, 3.50)

    def test_scan_item_product_not_found(self):
        # Add a product to the CheckoutRegister
        self.checkout_register._products.append(Product(456, "Milk, 2 Litres", "Fresh whole milk", 3.50))

        # Scan a product with an invalid barcode
        self.checkout_register.scan_item(9999)

        # Check if the total amount due remains unchanged
        self.assertEqual(self.checkout_register._total_amount_due, 0.0)

    def test_accept_payment_positive_amount(self):
        # Set the total amount due to $5.50
        self.checkout_register._total_amount_due = 5.50

        # Accept payment of $2.50
        self.checkout_register.accept_payment(2.50)

        # Check if the amount received and total amount due are updated correctly
        self.assertEqual(self.checkout_register._amount_received, 2.50)
        self.assertEqual(self.checkout_register._total_amount_due, 3.0)

    def test_accept_payment_negative_amount(self):
        # Set the total amount due to $5.50
        self.checkout_register._total_amount_due = 5.50

        # Attempt to accept a negative payment (should raise a ValueError)
        with self.assertRaises(ValueError):
            self.checkout_register.accept_payment(-2.50)

    def test_init(self):
        # Check if the CheckoutRegister is initialized correctly
        self.assertEqual(self.checkout_register._products, [])
        self.assertEqual(self.checkout_register._total_amount_due, 0.0)
        self.assertEqual(self.checkout_register._amount_received, 0.0)

if __name__ == '__main__':
    unittest.main()
