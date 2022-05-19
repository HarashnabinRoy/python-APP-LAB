import sqlite3

connection = sqlite3.connect('q3.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    product_id integer,
    unit_price integer,
    quantity integer
)""")

orders = [
    (101, 1, 450, 2), 
    (102, 2, 500, 3),
    (321, 4, 253, 5)

]

cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)

cursor.execute("""CREATE TABLE products (
    product_id integer PRIMARY KEY,
    product_name text,
    unit_price integer,
    supplier_id integer,
    package integer,
    order_id integer,
    FOREIGN KEY (order_id) REFERENCES orders (order_id)
)""")

products = [
    (1, "material ui", 450, 1, 5, 101),
    (2, "tailwind css", 500, 2, 6, 102),
    (321, "registration number", 321, 3, 7, 103)
]

cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", products)

cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
print(orders)
print('-----------------------------------------------------')
print(products)
print("-----------------------------------------------------")

cursor.execute("SELECT product.package-orde.quantity FROM products product, orders orde WHERE product.order_id = orde.order_id")
products = cursor.fetchall()
print(products)
print("-----------------------------------------------------")

cursor.execute("SELECT unit_price FROM products ORDER BY supplier_id DESC")
products = cursor.fetchall()
print(products)
print('-----------------------------------------------------')

cursor.execute("SELECT product_name, supplier_id, order_id FROM products")
products = cursor.fetchall()
print(products)

connection.commit()

connection.close()
