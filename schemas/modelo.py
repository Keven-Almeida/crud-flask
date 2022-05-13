from ma import ma 
from models.modelo import ModeloModel

class ModeloSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ModeloModel
        load_instance = True