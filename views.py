from flask import Flask, request, render_template, redirect, url_for
from controllers.modelo import Modelo, ModeloList
from models.modelo import ModeloModel

modelos_list = ModeloList()
modelo = Modelo()

def init_app(app: Flask):
    
    @app.route('/', methods=['GET'])
    def index():    
        result = modelos_list.get()
        return render_template('pages/index.html', modelos=result[0])
    
    @app.route('/search', methods=['POST'])
    def search():
        search = request.form['search']
        result = modelo.get(nome=search)
        
        if result[1] == 200:
            return render_template('pages/index.html', modelos=result)
        return render_template('pages/index.html', modelos=result)
    
    @app.route('/add', methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            nome = request.form['nome']
            descricao = request.form['descricao']
            model = ModeloModel,{'nome': nome,'descricao': descricao}
            modelos_list.post(model[1])
            redirect(url_for('index'))
            
        return render_template('pages/add.html')
    
    @app.route('/add/<string:nome>')
    def error(nome):    
        return render_template('pages/error.html', nome=nome)