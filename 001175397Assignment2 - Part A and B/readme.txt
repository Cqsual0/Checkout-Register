Credentials for supermarket admin 

Username - admin 
Password - admin 

Product Table:
(111, 'Chips', 'Salt and Vinegar chips', 3.99) 
(222, 'Chocolate', 'Dark 40%', 2.99)
(333, 'Sponge', "Clean's all spills", 1.99)    
(444, 'Cat litter', 'Best cat litter', 6.99)   
(555, 'Coke', 'No sugar', 2.5)
(666, '30x pack pepsi', 'Pepsi 30x pack', 7.99)
(777, 'Milk', 'Dariy Milk', 4.0)

admin_system.py is used for an easy access diagram of sales data using matplot. 

checkoutregister.py controls the heart of the register classes for main_module.

main_module.py is the interface of the checkout register. 

SQLite.py holds all the infomation of both database tables held within the supermarket.db. 

Supermarket_Admin.py is the dashboard for the entire application you're able to do the following

a. Add Products to Database
b. List all Products in Database
c. Find a Product in the Database
d. List All Transactions
e. Display an Excel report of all transactions
f. Display Product Sales Graph
g. Exit

SupermarketDAO.py is similar to the checkoutregister.py but instead holds classes for all of the application and is especially used within the supermarket admin 

test_product.py & testing.py are still outdated and were used for pervious version's of the application. 

