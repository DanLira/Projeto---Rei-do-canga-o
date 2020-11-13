from app.models.DAO import DAOPedido
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.Pedido import Pedido
import json
        


def add_pedido(_pedido):
    try:
        _id_user = str(_pedido['idUser'])
        
        return DAOPedido.add_pedido(p)
    except Exception as ex:
        print(ex)


def listarPedidos():
    try:
        return DAOPedido.listarPedidos()
    except Exception as ex:
        print(ex)
    

def getPedidoById(id):
    try:
        return DAOPedido.gePedidotById(id)
    except Exception as ex:
        print(ex)
    

def update_pedido(p):
    try:
        return DAOPedido.update_pedido(p)
    except Exception as ex:
        print(ex)
       

def delete_pedido(id):
    try:
        return DAOPedido.delete_pedido(id)
    except Exception as ex:
        print(ex)
    