import sqlite3
import json

airports_file_name="database/airports.json"
cities_file_name="database/cities.json"
countries_file_name="database/countries.json"

# Waiting to have data from an external API
data_flights=[
    ['Air France', 'Paris (CDG)', 'New York (JFK)', 8.0 , 11.0, 450, "€"],
    ['Easyjet', 'Lyon (LYS)', 'Londres (LHR)', 9.5 , 10.5, 120, "€"],
    ['Ryanair',  'Marseille (MRS)', 'Madrid (MAD)', 14.0 , 15.5, 80, "€"]
]

connection = sqlite3.connect('database/database.db')

# Opening JSON files for the airports, cities and countries data
with open(airports_file_name, encoding="utf8") as json_file:
    data_airports = json.load(json_file)

with open(cities_file_name, encoding="utf8") as json_file:
    data_cities = json.load(json_file)

with open(countries_file_name, encoding="utf8") as json_file:
    data_countries = json.load(json_file)

#open DB or create a new one if doesn't exist 
connection = sqlite3.connect('database/database.db')

#Open the file containing the base of the SQL and execute the SQL statements
with open('database/schema.sql') as f:
    connection.executescript(f.read())

#Insert value in the DB
cur = connection.cursor()

# Adding info into the countries table
i = 0
for element in data_countries["data"]:
    cur.execute("INSERT INTO countries (id, country_iso2, country_name) VALUES (?, ?, ?)",
                (data_countries["data"][i]["id"],
                data_countries["data"][i]["country_iso2"],
                data_countries["data"][i]["country_name"])
                )
    i+=1

# Adding info into the cities table
i = 0
for element in data_cities["data"]:
    #found value iata_code for city null --> got to fix it
    value_iata_code = i if not data_cities["data"][i]["iata_code"] else data_cities["data"][i]["iata_code"]

    cur.execute("INSERT INTO cities (id, city_name, iata_code, country_iso2) VALUES (?, ?, ?, ?)",
                (data_cities["data"][i]["id"],
                data_cities["data"][i]["city_name"], 
                value_iata_code,
                data_cities["data"][i]["country_iso2"])
                )
    i+=1

# Adding info into the airport table
i = 0
for element in data_airports["data"]:
    
    cur.execute("INSERT INTO airports (id, name, iata_code,icao_code, city_iata_code, country_name) VALUES (?, ?, ?, ?, ?, ?)",
                (data_airports["data"][i]["airport_id"],
                data_airports["data"][i]["airport_name"],
                data_airports["data"][i]["iata_code"], 
                data_airports["data"][i]["icao_code"],
                data_airports["data"][i]["city_iata_code"],
                data_airports["data"][i]["country_name"])
                )
    i+=1



# Adding info into the result table
for element in data_flights:
    cur.execute("INSERT INTO results (company, start_city, arrival_city, start_hour, arrival_hour, price, unit) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (element[0],
                element[1],
                element[2],
                element[3],
                element[4],
                element[5],
                element[6])
                )

#Implement changes into DB
connection.commit()

#close DB
connection.close()

print("######### Database update done #########")