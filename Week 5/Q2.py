import sqlite3

connection = sqlite3.connect('q2.db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE movies (movie_id integer, movie_name text, genre text, language text, rating real)")

movies = [
    (101, "kgf2", "action", "hindi", 8.5),
    (102, "spiderman", "superhero", "english", 8.1),
    (103, "doctor strange", "mystic", "english", 8.7),
    (321, "registration number", "RIP", "english",3.6)

]

cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", movies)

cursor.execute("UPDATE movies SET rating = (rating + (rating * 0.1))")
cursor.execute("SELECT movie_name, rating from movies")
movies = cursor.fetchall()
print(movies)
print('-----------------------------------------------------')

cursor.execute("DELETE from movies WHERE movie_id = 102")
cursor.execute("SELECT * FROM movies")
d = cursor.fetchall()
print(d)
print('-----------------------------------------------------')

cursor.execute("SELECT movie_name, rating FROM movies WHERE rating > 3")
r = cursor.fetchall()
print(r)
print('-----------------------------------------------------')

connection.commit()

connection.close()
