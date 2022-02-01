# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class BaseConfig():

    SQLALCHEMY_DATABASE_URI        = 'sqlite:///' + os.path.join(BASE_DIR, 'apidata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
