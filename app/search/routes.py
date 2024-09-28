from flask import render_template, request, url_for, redirect # type: ignore
from app.search import bp
from app.models.search import JsonReader
import os

@bp.route('/' , methods=('GET', 'POST'))
def index():
    return render_template('search/index.html')

@bp.route('/resultat/')
def results():
    data = JsonReader("app/static/database/countries.json")
    #data = os.getcwd()
    return render_template('search/resultat.html', data = data.get_data())