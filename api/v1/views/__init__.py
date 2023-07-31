#!/usr/bin/python3
"""Blueprint for API"""
from flask import Blueprint
<<<<<<< HEAD
=======

>>>>>>> e7851eb22dddb04d5af4b1ac6691b7ee52da657b
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
<<<<<<< HEAD
=======



>>>>>>> e7851eb22dddb04d5af4b1ac6691b7ee52da657b
