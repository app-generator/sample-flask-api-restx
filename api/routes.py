# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import request
from flask_restx import Api, Resource, fields

from api.models import db, Datas

rest_api = Api(version="1.0", title="Datas API")

"""
API Interface:
   
   - /datas
       - GET: return all items
       - POST: create a new item
   
   - /datas/:id
       - GET    : get item
       - PUT    : update item
       - DELETE : delete item
"""

"""
Flask-RestX models Request & Response DATA
"""

# Used to validate input data for creation
create_model = rest_api.model('CreateModel', {"data": fields.String(required=True, min_length=1, max_length=255)})

# Used to validate input data for update
update_model = rest_api.model('UpdateModel', {"data": fields.String(required=True, min_length=1, max_length=255)})

"""
    Flask-Restx routes
"""

@rest_api.route('/api/datas')
class Items(Resource):

    """
       Return all items
    """
    def get(self):

        items = Datas.query.all()
        
        return {"success" : True,
                "msg"     : "Items found ("+ str(len( items ))+")",
                "datas"   : str( items ) }, 200

    """
       Create new item
    """
    @rest_api.expect(create_model, validate=True)
    def post(self):

        # Read ALL input  
        req_data = request.get_json()

        # Get the information    
        item_data = req_data.get("data")

        # Create new object
        new_item = Datas(data=item_data)

        # Save the data
        new_item.save()
        
        return {"success": True,
                "msg"    : "Item successfully created ["+ str(new_item.id)+"]"}, 200

@rest_api.route('/api/datas/<int:id>')
class ItemManager(Resource):

    """
       Return Item
    """
    def get(self, id):

        item = Datas.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        return {"success" : True,
                "msg"     : "Successfully return item [" +str(id)+ "]",
                "data"    :  item.toJSON()}, 200

    """
       Update Item
    """
    @rest_api.expect(update_model, validate=True)
    def put(self, id):

        item = Datas.get_by_id(id)

        # Read ALL input from body  
        req_data = request.get_json()

        # Get the information    
        item_data = req_data.get("data")

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        item.update_data(item_data)
        item.save()

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully updated",
                "data"    :  item.toJSON()}, 200 

    """
       Delete Item
    """
    def delete(self, id):

        # Locate the Item
        item = Datas.get_by_id(id)

        if not item:
            return {"success": False,
                    "msg": "Item not found."}, 400

        # Delete and save the change
        Datas.query.filter_by(id=id).delete()
        db.session.commit()

        return {"success" : True,
                "msg"     : "Item [" +str(id)+ "] successfully deleted"}, 200                           
