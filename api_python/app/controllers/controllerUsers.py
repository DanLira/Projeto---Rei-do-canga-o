from app.models.DAO import DAOUsuario
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.User import User
        


def add_user(user):
    return DAOUsuario.add_user(user)

def listarUsers():
    return DAOUsuario.listarUsers()

def getById(id):
    return DAOUsuario.getById(id)

def update_user():
    return DAOUsuario.update_user()   

def delete_user(id):
    return DAOUsuario.delete_user(id)