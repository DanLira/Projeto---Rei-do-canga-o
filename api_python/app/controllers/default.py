#import pymysql
from app import app
from app.controllers import controllerUsers
from app.controllers import controllerEmpregado
from app.controllers import controllerFornecedorPF
from app.controllers import controllerFornecedorPJ
from config import mysql
from flask import Flask, request, flash, render_template, redirect, jsonify
from app.models.classes_basicas.User import User
from app.models.classes_basicas.Empregado import Empregado
from app.models.classes_basicas.FornecedorPF import FornecedorPF
from app.models.classes_basicas.FornecedorPJ import FornecedorPJ 
import json


@app.route("/index")
@app.route("/")
def index():
    return "index"


###ROTAS DE USERS

@app.route("/users",  methods=["POST"])
def add_user():
    _json = request.json
    _username = str(_json['userName'])
    _senha = str(_json['senha']) 
    _tipo = str(_json['tipo'])
    _id_empregado = str(_json['idEmpregado'])
    _status = str(_json['status'])
    user = User(_username, _senha, _tipo, _id_empregado, _status) 
    return controllerUsers.add_user(user)    

@app.route("/users",  methods=['GET'])
def listarUsers():
    return controllerUsers.listarUsers()

@app.route("/users/<int:id>",  methods=['GET'])
def getUserById(id):
    return controllerUsers.getById(id)

@app.route("/users",  methods=["PUT"])
def update_user():
    _json = request.json
    _id_user = str(_json['idUser'])
    _username = str(_json['userName'])
    _senha = str(_json['senha']) 
    _tipo = str(_json['tipo'])
    _id_empregado = int(_json['idEmpregado'])
    _status = str(_json['status'])
    user = User(_username, _senha, _tipo, _id_empregado, _status)
    user.setIdUser(_id_user) 
    return controllerUsers.update_user(user)   


@app.route("/users", methods=['DELETE'])
def delete_user():
    _json = request.json
    _id_user = int(_json['idUser'])
    return controllerUsers.delete_user(_id_user)   



###ROTAS DE EMPREGADOS

@app.route("/empregados",  methods=["POST"])
def add_empregado():
    _json = request.json
    _nome_empregado = str(_json['nomeEmpregado'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
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
    _status = str(_json['status'])

    empregado = Empregado(_nome_empregado, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    empregado.setTelefone(_telefone)
    empregado.setComplemento(_complemento)
    empregado.setCep(_cep)  
    return controllerEmpregado.add_empregado(empregado)


@app.route("/empregados",  methods=['GET'])
def listarEmpregados():
    return controllerEmpregado.listarEmpregados()


@app.route("/empregados/<int:id>",  methods=['GET'])
def getEmpregadoById(id):
    return controllerEmpregado.getById(id)


@app.route("/empregados",  methods=["PUT"])
def update_empregado():
    _json = request.json
    _id_empregado = str(_json['idEmpregado'])
    _nome_empregado = str(_json['nomeEmpregado'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
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
    _status = str(_json['status'])
    

    empregado = Empregado(_nome_empregado, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    empregado.setTelefone(_telefone)
    empregado.setComplemento(_complemento)
    empregado.setCep(_cep) 
    return controllerEmpregado.update_empregado(empregado)


@app.route("/empregados", methods=['DELETE'])
def delete_empregado():
    _json = request.json
    _id_empregado = str(_json['idEmpregado'])
    return controllerEmpregado.delete_empregado(_id_empregado) 



##ROTAS DE FORNECEDORESPF

@app.route("/fornecedorespf",  methods=["POST"])
def add_fornecedorpf():
    _json = request.json
    _nome_fornecedorpf = str(_json['nomeFornecedorPF'])
    _nick_name = str(_json['nickName'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
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
    _status = str(_json['status'])

    fornecedorpf = FornecedorPF(_nome_fornecedorpf, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpf.setNickName(_nick_name)
    fornecedorpf.setTelefone(_telefone)
    fornecedorpf.setComplemento(_complemento)
    fornecedorpf.setCep(_cep)
    return controllerFornecedorPF.add_fornecedorpf(fornecedorpf)


@app.route("/fornecedorespf",  methods=['GET'])
def listarFornecedorespf():
    return controllerFornecedorPF.listarFornecedorespf()


@app.route("/fornecedorespf/<int:id>",  methods=['GET'])
def getFornecedorPFById(id):
    return controllerFornecedorPF.getFornecedorPFById(id)


@app.route("/fornecedorespf",  methods=["PUT"])
def update_fornecedorpf():
    _json = request.json
    _id_fornecedorpf = str(_json['idFornecedorPF'])
    _nome_fornecedorpf = str(_json['nomeFornecedorPF'])
    _nick_name = str(_json['nickName'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
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
    _status = str(_json['status'])

    fornecedorpf = FornecedorPF(_nome_fornecedorpf, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpf.setIdFornecedorPF(_id_fornecedorpf)
    fornecedorpf.setNickName(_nick_name)
    fornecedorpf.setTelefone(_telefone)
    fornecedorpf.setComplemento(_complemento)
    fornecedorpf.setCep(_cep)
    return controllerFornecedorPF.update_fornecedorpf(fornecedorpf)


@app.route("/fornecedorespf", methods=['DELETE'])
def delete_fornecedorpf():
    _json = request.json
    _id_fornecedorpf = str(_json['idFornecedorPF'])
    return controllerFornecedorPF.delete_fornecedorpf(_id_fornecedorpf)


##ROTAS DE FORNECEDORESPJ

@app.route("/fornecedorespj",  methods=["POST"])
def add_fornecedorpj():
    _json = request.json
    _razao_social = str(_json['razaoSocial'])
    _nome_fantasia = str(_json['nomeFantasia'])
    _nick_name = str(_json['nickName'])
    _cnpj = str(_json['cnpj']) 
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
    _status = str(_json['status'])

    fornecedorpj = FornecedorPJ(_razao_social, _nome_fantasia, _cnpj, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpj.setNickName(_nick_name)
    fornecedorpj.setTelefone(_telefone)
    fornecedorpj.setComplemento(_complemento)
    fornecedorpj.setCep(_cep)
    return controllerFornecedorPJ.add_fornecedorpj(fornecedorpj)


@app.route("/fornecedorespj",  methods=['GET'])
def listarFornecedorespj():
    return controllerFornecedorPJ.listarFornecedorespj()

@app.route("/fornecedorespj/<int:id>",  methods=['GET'])
def getFornecedorPJById(id):
    return controllerFornecedorPJ.getFornecedorPJById(id)

@app.route("/fornecedorespj",  methods=["PUT"])
def update_fornecedorpj():
    _json = request.json
    _id_fornecedorpj = str(_json['idFornecedorPJ'])
    _razao_social = str(_json['razaoSocial'])
    _nome_fantasia = str(_json['nomeFantasia'])
    _nick_name = str(_json['nickName'])
    _cnpj = str(_json['cnpj']) 
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
    _status = str(_json['status'])

    fornecedorpj = FornecedorPJ(_razao_social, _nome_fantasia, _cnpj, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpj.setIdFornecedorPJ(_id_fornecedorpj)
    fornecedorpj.setNickName(_nick_name)
    fornecedorpj.setTelefone(_telefone)
    fornecedorpj.setComplemento(_complemento)
    fornecedorpj.setCep(_cep)
    return controllerFornecedorPJ.update_fornecedorpj(fornecedorpj)


@app.route("/fornecedorespj", methods=['DELETE'])
def delete_fornecedorpj():
    _json = request.json
    _id_fornecedorpj = str(_json['idFornecedorPJ'])
    return controllerFornecedorPJ.delete_fornecedorpj(_id_fornecedorpj)