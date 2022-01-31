# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - present AppSeed.us
"""

from api import app, db

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
