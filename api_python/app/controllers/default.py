#import pymysql
from app import app
from app.controllers import controllerUsers
from config import mysql
from flask import Flask, request, flash, render_template, redirect, jsonify
from app.models.classes_basicas.User import User
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

    user = User(_username, _senha, _tipo, _id_empregado) 
    
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

    user = User(_username, _senha, _tipo, _id_empregado)
    user.setIdUser(_id_user) 
    
    return controllerUsers.update_user(user)   


@app.route("/users", methods=['DELETE'])
def delete_user():
    _json = request.json
    _id_user = str(_json['id_user'])

    return controllerUsers.delete_user(_id_user)   





