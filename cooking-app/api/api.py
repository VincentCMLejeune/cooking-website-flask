import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/recipes-list')
def get_recipes_list():
    return {'recipes': ['recipe1', 'recipe2', 'recipe3']}
