import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO results (company, start_city, arrival_city, start_hour, arrival_hour, price, unit) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Air France', 'Paris (CDG)', 'New York (JFK)', 8.0 , 11.0, 450, "€")
            )

cur.execute("INSERT INTO results (company, start_city, arrival_city, start_hour, arrival_hour, price, unit) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Easyjet', 'Lyon (LYS)', 'Londres (LHR)', 9.5 , 10.5, 120, "€")
            )

cur.execute("INSERT INTO results (company, start_city, arrival_city, start_hour, arrival_hour, price, unit) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('Ryanair',  'Marseille (MRS)', 'Madrid (MAD)', 14.0 , 15.5, 80, "€")
            )

connection.commit()
connection.close()