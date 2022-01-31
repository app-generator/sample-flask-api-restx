# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request
from flask_restx import Api, Resource, fields

from api.models import db, Datas
from api.config import BaseConfig

rest_api = Api(version="1.0", title="Datas API")

'''

API Interface:
   
   - /datas
       - GET: return all datas
       - POST: create a new data
   
   - /datas/:id
       - GET    : get specific data
       - POST   : update 
       - DELETE : update

'''


"""
    Flask-Restx models Request & Response DATA
"""

create_model = rest_api.model('CreateModel', {"data": fields.String(required=True, min_length=1, max_length=100)
                                            })

"""
    Flask-Restx routes
"""

@rest_api.route('/api/datas')
class Register(Resource):

    """
       Return all data
    """
    def get(self):

        return {"success" : True,
                "msg"     : "return all data"}, 200

    @rest_api.expect(create_model, validate=True)
    def post(self):

        # read input    
        req_data = request.get_json()

        # Get the information    
        _data = req_data.get("data")

        # Create new object
        new_data = Datas(data=_data)

        # Save the data
        new_data.save()
        
        return {"success": True,
                "msg"    : "Item successfully created ["+ str(new_data.id)+"]"}, 200

@rest_api.route('/api/datas/<int:id>')
class GetItem(Resource):

    """
       Return specific Item
    """
    def get(self, id):

        _data = Datas.get_by_id(id)

        if not _data:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  _data.toJSON()}, 200
