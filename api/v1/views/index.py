#!/usr/bin/python3
# index.py

'''api status'''
from flask import jsonify
from api.v1.views import app_views
import models
from models import storage
from models.base_model import BaseModel


app.url_map.strict_slashes = False


@app_views.route('/status')
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats')
def stuff():
    '''JSON Responses'''
    todos = {
            'states': State, 'users': User,
            'amenities': Amenity, 'cities': City,
            'places': Place, 'reviews': Review
            }
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)
