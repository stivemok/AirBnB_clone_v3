#!/usr/bin/python3
"""Index view for API"""
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views


@app_views.route('/', methods=['GET'], strict_slash=False)
def Hello_world():
    '''Gets the status of the API'''
    return ("Hello_world")


@app_views.route('/status', methods=['GET'], strict_slash=False)
def get_status():
    '''Gets the status of the API'''
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slash=False)
def get_stats():
    """retrives the number of each objects by type"""
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
