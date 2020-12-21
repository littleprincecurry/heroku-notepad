from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from os import environ
import json

app = Flask(__name__)
app.config['MONGO_URI'] = environ.get(
    'MONGODB_URI') or 'mongodb://localhost:27017/heroku-notepad'

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html', name='Scot')


@app.route('/tasks')
def tasks():
    tasks = mongo.db.tasks.find({})
    data = []

    for task in tasks:
        item = {
            '_id': str(task['_id']),
            'description': task['description']
        }
        data.append(item)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
