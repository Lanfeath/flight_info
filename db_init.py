for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    airport = Airport(name=f'Airport #{random_num}',
                iata_code=f'Iata {random_num}',
                icao_code=f'Icao {random_num}',
                city_iata_code=f'City_Iata {random_num}',
                country_name=f'Country {random_num}')
    db.session.add(airport)
    print(airport.name)
    print(airport.iata_code)
    print('--')
    db.session.commit()

import random
from app.extensions import db
from app.models.data import City, Country

for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    country = Country(name=f'Country #{random_num}', iso2= random_num)
    db.session.add(country)
    print(country.name)
    print('--')
    db.session.commit()

for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    city = City(name=f'City #{random_num}',
                iata_code=f'Iata {random_num}',
                country_iso2= random_num)
    db.session.add(city)
    print(city.name)
    print(city.iata_code)
    print('--')
    db.session.commit()