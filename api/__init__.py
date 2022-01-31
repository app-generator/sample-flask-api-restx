# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json

from flask import Flask
from flask_cors import CORS

from api.routes import rest_api
from api.models import db

app = Flask(__name__)

app.config.from_object('api.config.BaseConfig')

db.init_app(app)
rest_api.init_app(app)
CORS(app)

# Setup database
@app.before_first_request
def initialize_database():
    db.create_all()

