from flask import jsonify, render_template
from controllers.modelo import Modelo
from ma import ma   
from db import db

import views 

from marshmallow import ValidationError
from controllers.modelo import ModeloList

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

views.init_app(app)

db.init_app(app)
if __name__ == '__main__':
    ma.init_app(app)
    server.run()

