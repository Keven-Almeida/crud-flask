from flask import request
from flask_restplus import Resource, fields

from models.modelo import ModeloModel
from schemas.modelo import ModeloSchema

from server.instance import server

modelo_ns = server.modelo_ns

modelo_schema = ModeloSchema()
modelo_list_schema = ModeloSchema(many=True)

ITEM_NOT_FOUND = "Modelo not found."
ITEM_DELETED = "Model successfully deleted."

# Model required by flask_restplus for expect
item = modelo_ns.model('Modelo', {
    'nome': fields.String('nome do modelo'),
    'descricao': fields.String('descrição do modelo'),
})


class Modelo(Resource):

    def get(self, id):
        modelo_data = ModeloModel.find_by_id(id)
        if modelo_data:
            return modelo_schema.dump(modelo_data), 200
        return {'message': ITEM_NOT_FOUND}, 404

    def get(self, nome):
        modelo_data = ModeloModel.find_by_nome(nome)
        if modelo_data:
            return modelo_schema.dump(modelo_data), 200
        return {'message': ITEM_NOT_FOUND}, 404
    
    def delete(self, nome):
        modelo_data = ModeloModel.find_by_nome(nome)
        if modelo_data:
            modelo_data.delete_from_db()
            return {'message': ITEM_DELETED}, 204
        return {'message': ITEM_NOT_FOUND}, 404

    @modelo_ns.expect(item)
    def put(self, nome):
        modelo_data = ModeloModel.find_by_nome(nome)
        modelo_json = request.get_json()

        if modelo_data:
            modelo_data.nome = modelo_json['nome']
            modelo_data.descricao = modelo_json['descricao']
        else:
            modelo_data = modelo_schema.load(modelo_json)

        modelo_data.save_to_db()
        return modelo_schema.dump(modelo_data), 200


class ModeloList(Resource):
    @modelo_ns.doc('Get all the models')
    def get(self):
        return modelo_list_schema.dump(ModeloModel.find_all()), 200

    @modelo_ns.expect(item)
    @modelo_ns.doc('Create an model')
    def post(self):
        modelo_json = request.get_json()
        modelo_data = modelo_schema.load(modelo_json)

        modelo_data.save_to_db()

        return modelo_schema.dump(modelo_data), 201