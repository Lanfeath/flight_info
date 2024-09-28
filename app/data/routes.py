from flask import render_template # type: ignore
from app.data import bp
from app.extensions import db
from app.models.data import Airport, Country, City

@bp.route('/')
def index():
    return render_template('data/index.html')

@bp.route('/Countries')
def countries():
    countries=Country.query.all()
    return render_template('data/countries.html', countries=countries)

@bp.route('/Cities')
def cities():
    cities=City.query.all()
    return render_template('data/cities.html', cities=cities)

@bp.route('/Airports')
def airports():
    airports=Airport.query.all()
    return render_template('data/airports.html', airports=airports)