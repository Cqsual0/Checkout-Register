import datetime
from checkoutRegister import CheckoutRegister
from SupermarketDAO import SupermarketDAO
from Product import Product
from Transaction import Transaction
import sqlite3

# README holds all info and products for testing

def print_receipt(checkout_register, change_due):
    print("\n--- Receipt ---")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nItems Purchased:")
    for product in checkout_register._scanned_products:
        print(f"{product['name']} - ${product['price']:.2f}")
    print(f"\nTotal Paid: ${checkout_register._total_paid:.2f}")
    print(f"Change Given: ${change_due:.2f}")
    print("\nThank you for shopping with us!")
    print("--- End of Receipt ---\n")

def main():
    # Initialize the checkout register
    checkout_register = CheckoutRegister()
    checkout_register.dao = SupermarketDAO('supermarket.db')

    # Load product data from the product data file
    checkout_register.load_product_data()

    while True:
        # Start the checkout process
        while True:
            product_barcode = input("Please enter the barcode of your item: ")
            try:
                product_barcode = int(product_barcode)
            except ValueError:
                print("ERROR!! – scanned barcode is incorrect")
                continue

            if checkout_register.dao.findProduct(product_barcode):
                checkout_register.scan_item(product_barcode)
            else:
                print(f"Error: Product with barcode {product_barcode} not found.")

            choice = input("Would you like to scan another item? (Y/N): ").upper()
            if choice == 'N':
                break

        # Payment process
        change_due = 0.0
        while checkout_register._total_amount_due > 0:
            try:
                amount_paid = float(input(f"Total amount due: ${checkout_register._total_amount_due:.2f}. Please enter an amount to pay: "))
                change_due = checkout_register.accept_payment(amount_paid)

                if checkout_register._total_amount_due > 0:
                    print(f"Remaining amount due: ${checkout_register._total_amount_due:.2f}")
                else:
                    if change_due > 0:
                        print(f"Change due: ${change_due:.2f}")
                    break  # Break out of the loop if no amount is due

            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        # Print receipt
        print_receipt(checkout_register, change_due)

        # Save the transaction
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        checkout_register.save_transaction(current_date)  # Updated to pass only the date

        # Reset the transaction details for the next customer
        checkout_register.reset_transaction()

        next_customer = input("Do you want to start a new transaction? (Y/N): ").upper()
        if next_customer == 'Y':
            continue  # This will start a new iteration of the while loop for the next customer.
        else:
            print("Thank you for using our system!")
            break  # This will exit the while loop and end the program.

if __name__ == "__main__":
    main()
