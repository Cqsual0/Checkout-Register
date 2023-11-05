import sqlite3
import matplotlib.pyplot as plt

# Initialize lists for product names and quantities sold
product_names = []
quantities_sold = []

# Connect to the new database
conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()

# Create a dictionary to store product quantities
product_quantities = {}

# Query the database to retrieve transaction data
cursor.execute("SELECT Barcode, Amount FROM Transactions")
transactions = cursor.fetchall()

# Count quantities sold for each product
for barcode, amount in transactions:
    if barcode in product_quantities:
        product_quantities[barcode] += amount
    else:
        product_quantities[barcode] = amount

# Query the database to retrieve product names using barcodes
for barcode in product_quantities.keys():
    cursor.execute("SELECT Name FROM Products WHERE Barcode = ?", (barcode,))
    product_name = cursor.fetchone()[0]
    product_names.append(product_name)
    quantities_sold.append(product_quantities[barcode])

# Create a bar chart
plt.bar(product_names, quantities_sold)
plt.xlabel('Product Names')
plt.ylabel('Quantities Sold')
plt.title('Products Sold by Quantity')
plt.xticks(rotation=90)

# Display the bar chart
plt.show()

# Close the database connection
conn.close()
