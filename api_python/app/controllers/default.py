import pymysql
from app import app
from app.controllers import controllerUsers
from config import mysql
from flask import flash, render_template, request, redirect 
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastroempregado")
def cadastroempregado():
    return "Cadastro de empregado aqui"


@app.route("/cadastrocliente")
def cadastrocliente():
    return "Cadastro de Cliente Page"

@app.route("/cadastroforncedor")
def cadastrofornecedor():
    return "Cadastro de Fornecedor Page"

@app.route("/gerarpedido")
def gerarpedido():
    return "Cadastro de pedido Page"

@app.route("/cadastroproduto")
def cadastroproduto():
    return "Cadastro de Produto Page"

@app.route("/users",  methods=['POST'])
def add_user():
    return controllerUsers.DAOUsuario.add_user()    

@app.route("/users",  methods=['GET'])
def listarUsers():
    return controllerUsers.DAOUsuario.users()

@app.route("/users/<int:id>",  methods=['GET'])
def getById(id):
    return controllerUsers.DAOUsuario.getById(id)

# @app.route("/users",  methods=['PUT'])
# def cadastrousuario():
#     return controllerUsers.DAOUsuario

# @app.route("/users/<int:id>", methods=['DELETE'])
# def cadastrousuario():
#     return controllerUsers.DAOUsuario    

@app.route("/cadastrovendedor")
def cadastrovendedor():
    return "Cadastro de Vendedor Page"

