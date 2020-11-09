#import pymysql
from app import app
from app.controllers import controllerUsers
from config import mysql
from flask import Flask, request, flash, render_template, redirect, jsonify
from app.models.classes_basicas.User import User
from app.models.classes_basicas.Empregado import Empregado
import json


@app.route("/index")
@app.route("/")
def index():
    return "index"


@app.route("/users",  methods=["POST"])
def add_user():
    _json = request.json
    _username = str(_json['username'])
    _senha = str(_json['senha']) 
    _tipo = str(_json['tipo'])
    _id_empregado = str(_json['id_empregado'])
    _status = str(_json['status'])
    user = User(_username, _senha, _tipo, _id_empregado, _status) 
    return controllerUsers.add_user(user)    

@app.route("/users",  methods=['GET'])
def listarUsers():
    return controllerUsers.listarUsers()

@app.route("/users/<int:id>",  methods=['GET'])
def getById(id):
    return controllerUsers.getById(id)

@app.route("/users",  methods=["PUT"])
def update_user():
    _json = request.json
    _id_user = str(_json['id_user'])
    _username = str(_json['username'])
    _senha = str(_json['senha']) 
    _tipo = str(_json['tipo'])
    _id_empregado = int(_json['id_empregado'])
    _status = str(_json['status'])
    user = User(_username, _senha, _tipo, _id_empregado, _status)
    user.setIdUser(_id_user) 
    return controllerUsers.update_user(user)   


@app.route("/users", methods=['DELETE'])
def delete_user():
    _json = request.json
    _id_user = str(_json['id_user'])
    return controllerUsers.delete_user(_id_user)   



###ROTAS DE EMPREGADOS

@app.route("/empregados",  methods=["POST"])
def add_empregado():
    _json = request.json
    _nome_empregado = str(_json['nome_empregado'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['data_nascimento'])
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])


    #empregado = Empregado() 
    return "ok"
    
    #return controllerUsers.add_user(user)

