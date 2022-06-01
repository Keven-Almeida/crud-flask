import json
import requests

from flask import Flask, request, render_template, redirect, url_for
from controllers.modelo import Modelo, ModeloList
from models.modelo import ModeloModel

modelos_list = ModeloList()
model = Modelo()

def init_app(app: Flask):
    
    @app.route('/', methods=['GET'])
    def index():    
        result = modelos_list.get()
        return render_template('pages/index.html', modelos=result[0])
    
    @app.route('/search', methods=['POST'])
    def search():
        search = request.form['search']
        result = model.get(nome=search)
        
        if result[1] == 200:
            return render_template('pages/index.html', modelos=result)
        return render_template('pages/index.html', modelos=result)
    
    @app.route('/modelo', methods=['GET','POST',])
    def modelo():
        if request.method == 'POST':
            nome =  request.form['nome']
            descricao = request.form['descricao']
            model = dict(nome=nome, descricao=descricao)
            modelos_list.post(model)
            redirect(url_for('index'))
            
        return render_template('pages/modelo.html')
    
    @app.route('/modelo/<string:nome>')
    def error(nome):    
        return render_template('pages/error.html', nome=nome)