import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    ingredients = db.Column(db.String(500), unique=False, nullable=False)
    instructions = db.Column(db.String(1000), unique=False, nullable=False)
    temperature = db.Column(db.String(10), unique=False, nullable=False)
    isVegetarian = db.Column(db.Boolean, unique=False, default=False, nullable=False)
    isQuick = db.Column(db.Boolean, unique=False, default=False, nullable=False)
    isTuppable = db.Column(db.Boolean, unique=False, default=False, nullable=False)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/recipes-list')
def get_recipes_list():
    return {'recipes': ['recipe1', 'recipe2', 'recipe3']}
