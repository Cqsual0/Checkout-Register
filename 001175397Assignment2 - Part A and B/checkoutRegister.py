import sqlite3
from SupermarketDAO import SupermarketDAO
from Transaction import Transaction
import datetime

class CheckoutRegister:
    def __init__(self):
        self.dao = SupermarketDAO('supermarket.db')  # Include the database name when initializing SupermarketDAO
        self._scanned_products = []
        self._products = []  # Initialized to store product data
        self._total_amount_due = 0.0
        self._original_total_amount_due = 0.0  # To keep track of the original total
        self._total_paid = 0.0
        self._amount_received = 0.0  # To keep track of the total amount received
        self.change_given = 0.0

    def load_product_data(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('supermarket.db')
            cursor = conn.cursor()

            # Execute a query to retrieve product data
            cursor.execute("SELECT barcode, name, description, price FROM Product")
            product_data = cursor.fetchall()

            # Clear the existing products before loading new ones
            self._products.clear()

            # Process the retrieved data
            for row in product_data:
                barcode, name, description, price = row
                product = {"barcode": barcode, "name": name, "description": description, "price": price}
                self._products.append(product)

            # Close the database connection
            conn.close()

        except sqlite3.Error as e:
            print("Error: An error occurred while loading product data from the database:", e)

    def scan_item(self, product_barcode: int):
        print(f"Scanning product with barcode: {product_barcode}")

        product_found = None  # Initialize product_found to None
        for product in self._products:
            if product["barcode"] == product_barcode:
                product_found = product  # Store the matching product
                break

        if product_found is not None:
            print(f"Scanned Product: {product_found['name']} - Description: {product_found['description']} - Price: ${product_found['price']:.2f}")
            self._total_amount_due += product_found['price']
            self._original_total_amount_due = self._total_amount_due
            self._scanned_products.append(product_found)
        else:
            print(f"Error: Product with barcode {product_barcode} not found.")
        print(f"Current Total: ${self._total_amount_due:.2f}")

    def accept_payment(self, amount_paid: float):
        if amount_paid < 0:
            raise ValueError("Negative amounts are not accepted")

        self._amount_received += amount_paid
        if self._amount_received >= self._original_total_amount_due:
            self.change_given = self._amount_received - self._original_total_amount_due  # Calculate the change to give back
            self._total_paid = self._original_total_amount_due
            self._total_amount_due = 0
        else:
            self._total_paid += amount_paid
            self._total_amount_due -= amount_paid
            self.change_given = 0.0  # No change to give back if the payment is not complete

        return self.change_given


    def print_receipt(self):
        print("\n----- Final Receipt -----")
        for product in self._scanned_products:
            print(f"{product['name']}, {product['price']:.2f}")
        print(f"Total amount due: ${self._original_total_amount_due:.2f}")
        print(f"Total paid: ${self._total_paid:.2f}")
        print(f"Change given: ${self.change_given:.2f}\n")

    def save_transaction(self, date: str):
        # Aggregate the total amount of the transaction
        total_amount = sum(product['price'] for product in self._scanned_products)
        # Concatenate barcodes into a single string or use another way to represent multiple products
        barcodes = ','.join(str(product['barcode']) for product in self._scanned_products)
        
        # Create a single Transaction object for the entire transaction
        transaction = Transaction(date, barcodes, total_amount)
        self.dao.addTransactionToDB(transaction)

    def reset_transaction(self):
        self._scanned_products = []
        self._total_amount_due = 0.0
        self._total_paid = 0.0
        self._amount_received = 0.0
        # Do not reset self._products if you want it to persist across transactions

