from app.models.DAO import DAOPedido
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.Pedido import Pedido
from app.models.classes_basicas.Produto import Produto
import json
from datetime import date, datetime
        


def add_pedido(_pedido):
    try:
        idUser = _pedido['idUser']
        pedido = Pedido(idUser)
        data_atual = date.today()
        dataFormatada = data_atual.strftime('%d/%m/%Y')
        pedido.setDataPedido(dataFormatada)
        pedido.setStatusPedido("Finalizado")

        

        produto = Produto("PRODUTO 002", "KG", "10.59", 100000, "", "A")
        produto.setIdProduto(1009)
        produto.setQuantidade(500)

        produtob = Produto("TESTE", "KG", "1.59", 100000, "", "A")
        produtob.setIdProduto(1008)
        produtob.setQuantidade(10)


        produtoc = Produto("PRODUTO 002", "KG", "5.59", 100000, "", "A")
        produtoc.setIdProduto(1009)
        produtoc.setQuantidade(1)


        pedido.listaProdutos.append(produto)
        pedido.listaProdutos.append(produtob)
        pedido.listaProdutos.append(produtoc)
        
        return DAOPedido.add_pedido(pedido)
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
    