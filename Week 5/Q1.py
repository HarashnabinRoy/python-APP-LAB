from datetime import datetime
import sqlite3

connection = sqlite3.connect('q1.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE recipes (
    name text,
    description text,
    category_id integer,
    chef_id text,
   created timestamp
)""")

time = datetime.now()
recipes = [
    ("paneer masala", "p m", 101, "BL00001", time),
    ("chicken masala", "c m", 102, "BL00002", time),
    ("butter naan", "chinese", 103, "BL00003", time),
    ("registration number", "english", 321, "BL00321", time)

]

cursor.executemany("INSERT INTO recipes VALUES (?, ?, ?, ?, ?)", recipes)

cursor.execute("SELECT * FROM recipes")
recipes = cursor.fetchall()
print(len(recipes))
print("-----------------------------------------------------")

cursor.execute("SELECT * FROM recipes WHERE description = 'chinese'")
recipes = cursor.fetchall()
print(len(recipes))
print('-----------------------------------------------------')

cursor.execute("SELECT category_id, name FROM recipes WHERE chef_id = 'BL00002'")
r = cursor.fetchall()
print(r)
print('-----------------------------------------------------')

cursor.execute("SELECT description FROM recipes WHERE name LIKE 'p%'")
d = cursor.fetchall()
print(d)
print('-----------------------------------------------------')

connection.commit()

connection.close()
