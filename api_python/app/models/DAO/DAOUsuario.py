import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.User import User
        


def add_user(user):
    
    try:
        _hashed_password = generate_password_hash(user.getSenha())
        sql = "INSERT INTO USUARIOS(username, senha, tipo, id_empregado) VALUES(%s, %s, %s,%s)"
        data = (user.getUsername(), _hashed_password, user.getTipo(), user.getIdEmpregado())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return _hashed_password
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        

def listarUsers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_user, username, senha, tipo, id_empregado FROM usuarios")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e + "TESTE")
    finally:
        cursor.close() 
        conn.close()
        

def getById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_user, username, senha, tipo, id_empregado FROM usuarios WHERE id_user=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


def update_user(user):
    try:
        _hashed_password = generate_password_hash(user.getSenha())
        sql = "UPDATE USUARIOS SET username=%s, senha=%s, tipo=%s, id_empregado=%s WHERE id_user=%s"
        data = (user.getUsername(), _hashed_password, user.getTipo(), user.getIdEmpregado(), user.getIdUser())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        

def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "DELETE FROM USUARIOS WHERE id_user=%s"
        data = id
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
        
