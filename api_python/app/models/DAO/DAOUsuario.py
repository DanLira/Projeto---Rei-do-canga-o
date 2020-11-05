import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.User import User
		


def add_user():
	try:
		
		_json = request.json
		_tipo = _json['tipo']
		_login = _json['login']
		_senha = _json['senha']
		# validate the received values
		if _tipo and _login and _senha and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_senha)
			# save edits
			sql = "INSERT INTO tbl_user(user_tipo, user_login, user_senha) VALUES(%s, %s, %s)"
			data = (_tipo, _login, _hashed_password,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		

def users():
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

@app.route('/update', methods=['PUT'])
def update_user():
	try:
		_json = request.json
		_id = _json['id']
		_tipo = _json['tipo']
		_login = _json['login']
		_senha = _json['senha']		
		# validate the received values
		if _tipo and _login and _senha and _id and request.method == 'PUT':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_senha)
			# save edits
			sql = "UPDATE tbl_user SET user_tipo=%s, user_login=%s, user_senha=%s WHERE user_id=%s"
			data = (_tipo, _login, _hashed_password, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
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
		
