import sqlite3
from flask import Flask, render_template # type: ignore

def get_db_connection():
    conn = sqlite3.connect('database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def result():
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM results').fetchall()
    conn.close()
    return render_template('results.html', results=results)