# SupermarketDAO.py (No changes here)

# main_module.py
import sys
import datetime
from SupermarketDAO import SupermarketDAO
from Product import Product
from Transaction import Transaction
import pickle

# Load user credentials from the user_credentials.pkl file
def load_user_credentials():
    try:
        with open('user_credentials.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

def authenticate():
    # Load user credentials
    saved_credentials = load_user_credentials()
    
    if saved_credentials is None:
        print("No saved credentials found. Please contact the administrator for access.")
        return False
    
    saved_username, saved_password = saved_credentials
    entered_username = input("Username: ")
    entered_password = input("Password: ")

    if entered_username == saved_username and entered_password == saved_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Please try again.")
        return False

def main():
    authenticated = False
    while not authenticated:
        print("\nSupermarket Admin Login:")
        print("1. Login")
        print("2. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            authenticated = authenticate()
        elif choice == '2':
            print("Exiting the Supermarket Application.")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")
    
    # Rest of your script after authentication
    dao = SupermarketDAO('supermarket.db')

    while True:
        print("\nSupermarket Admin Menu:")
        print("a. Add Products to Database")
        print("b. List all Products in Database")
        print("c. Find a Product in the Database")
        print("d. List All Transactions")
        print("e. Display an Excel report of all transactions")
        print("f. Display Product Sales Graph")
        print("g. Exit")

        choice = input("Select an option: ")

        if choice == 'a':
            # Validate barcode
            while True:
                barcode = input("Enter the product's barcode: ")
                if barcode.strip() == '':
                    print("The barcode must not be blank. Please enter a valid barcode.")
                else:
                    break  # Exit loop if barcode is valid
            
            # Validate name
            while True:
                name = input("Enter the product's name: ")
                if name.strip() == '':
                    print("The product name must not be blank. Please enter a valid name.")
                else:
                    break  # Exit loop if name is valid
            
            # Validate description
            while True:
                description = input("Enter the product's description: ")
                if description.strip() == '':
                    print("The product description must not be blank. Please enter a valid description.")
                else:
                    break  # Exit loop if description is valid
            
            # Validate price
            while True:
                try:
                    price = float(input("Enter the product's price: "))
                    if price < 0:
                        print("The price must not be negative. Please enter a valid price.")
                    else:
                        break  # Exit loop if price is valid
                except ValueError:
                    print("Invalid input. Please enter a number for the price.")
            
            # Add product to database after validation
            product = Product(barcode, name, description, price)
            success = dao.addProductToDB(product)
            if success:
                print("Product added to the database successfully.")
            else:
                print("Failed to add the product to the database.")
        elif choice == 'b':
            products = dao.listAllProducts()
            if not products:
                print("No products found in the database.")
            else:
                for product in products:
                    print(product)
        elif choice == 'c':
            barcode = input("Enter the product barcode to search for: ")
            product = dao.findProduct(barcode)
            if product:
                print(product)
            else:
                print(f"Product with barcode {barcode} not found.")
        elif choice == 'd':
            transactions = dao.listAllTransactions()
            if not transactions:
                print("No transactions found in the database.")
            else:
                for transaction in transactions:
                    print(transaction)
        elif choice == 'e':
            filename = 'transactions_report.xlsx'
            dao.generate_excel_report(filename)
            print(f"Excel report saved as {filename}.")

        elif choice == 'f':
            dao.displayBarchartOfProductsSold()

        elif choice == 'g':
            # Exit the program
            print("Exiting the Supermarket Application.")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
