from db import db

class ModeloModel(db.Model):
    __tablename__ = 'modelos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True,)
    descricao = db.Column(db.String(255), nullable=True,)
    
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
    
    def __repr__(self):
        return f'ModeloModel(nome={self.nome}, descricao={self.descricao})'

    def json(self):
        return  {
            'nome': self.nome,
            'descricao': self.descricao
            },
    
    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        