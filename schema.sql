DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

DROP TABLE IF EXISTS results;

CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    company TEXT NOT NULL,
    start_city TEXT NOT NULL,
    arrival_city TEXT NOT NULL,
    start_hour FLOAT NOT NULL,
    arrival_hour FLOAT NOT NULL,
    price FLOAT NOT NULL,
    unit TEXT NOT NULL
);