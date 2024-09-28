from app.extensions import db

class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    iata_code = db.Column(db.String(50))
    icao_code = db.Column(db.String(50))
    city_iata_code = db.Column(db.String(50))
    country_name = db.Column(db.String(150))

    def __repr__(self):
        return f'<Airports "{self.name}">'

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    iata_code = db.Column(db.String(50))
    country_iso2 = db.Column(db.Integer)

    def __repr__(self):
        return f'<City "{self.name}">'

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    iso2 = db.Column(db.Integer)

    def __repr__(self):
        return f'<Country "{self.name}">'