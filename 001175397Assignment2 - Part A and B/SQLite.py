import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()

# View all records in the "Product" table
print("Product Table:")
cursor.execute('SELECT * FROM Product')
product_records = cursor.fetchall()
for product in product_records:
    print(product)

# View all records in the "Transactions" table
print("\nTransactions Table:")
cursor.execute('SELECT * FROM Transactions')
transaction_records = cursor.fetchall()
for transaction in transaction_records:
    print(transaction)

# Close the database connection
conn.close()
