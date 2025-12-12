from flask import Flask, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

engine = create_engine('sqlite:///movies.db')
connection = engine.connect()

@app.route('/')
def home():
    query = text('SELECT * FROM reviews;')
    result = connection.execute(query).fetchall()

    return render_template('index.html', movies=result)

app.run(debug=True, reloader_type='stat', port=5000)
