-- Need to put this for SQLLite
PRAGMA foreign_keys= ON;

DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id INTEGER PRIMARY KEY NOT NULL,
    country_iso2 INTEGER NOT NULL UNIQUE,
    country_name TEXT UNIQUE NOT NULL
);

DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    id INTEGER PRIMARY KEY NOT NULL,
    city_name TEXT NOT NULL,
    iata_code TEXT NOT NULL UNIQUE,
    country_iso2 INTEGER NOT NULL,
    FOREIGN KEY (country_iso2) REFERENCES countries(country_iso2) ON DELETE CASCADE
);

DROP TABLE IF EXISTS airports;

CREATE TABLE airports (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    iata_code TEXT NOT NULL,
    icao_code TEXT NOT NULL,
    city_iata_code INTEGER,
    country_name TEXT
    -- FOREIGN KEY (city_iata_code) REFERENCES cities(iata_code) ON DELETE CASCADE
);

DROP TABLE IF EXISTS results;

CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    start_city TEXT NOT NULL,
    arrival_city TEXT NOT NULL,
    start_hour FLOAT NOT NULL,
    arrival_hour FLOAT NOT NULL,
    price FLOAT NOT NULL,
    unit TEXT NOT NULL
);