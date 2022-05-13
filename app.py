from flask import jsonify
from resources.modelo import Modelo
from ma import ma   
from db import db

from marshmallow import ValidationError
from resources.modelo import ModeloList

from server.instance import server

api = server.api
app = server.app 

@app.before_first_request
def create_tables():
    db.create_all()

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400
api.add_resource(Modelo, '/modelo/<string:nome>')
api.add_resource(ModeloList, '/modelo')

db.init_app(app)
if __name__ == '__main__':
    ma.init_app(app)
    server.run()