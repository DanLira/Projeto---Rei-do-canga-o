import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.Empregado import User
		

@app.route('/create', methods=['POST'])
def add_empregado():
	try:
		
		_json = request.json
		_nome = _json['nome']
		_cpf = _json['cpf']
        _sexo = _json['sexo']
        _dataNascimento = _json['dataNascimento']
        _telefone = _json['telefone']
        _celular = _json['celular']
        _email = _json['email']
        _endereco = _json['endereco']
        _complemento = _json['complemento']
        _bairro = _json['bairro']
        _cep = _json['cep']
        _cidade = _json['cidade']
        _estado = _json['estado']
        _pais = _json['pais']


		# validate the received values
		if _nome and _cpf and _sexo and  _dataNascimento and _celular and _email and _endereco and _bairro and _cidade and _estado and _pais and request.method == 'POST':
			
			# save edits
			sql = "INSERT INTO EMPREGADOS(nome_empregado, cpf, sexo, data_nascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"
			data = (_nome, _cpf, _sexo, _dataNascimento, _telefone, _celular, _email, _endereco, _complemento, _bairro, _cep, _cidade, _estado, _pais)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Empregado added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/getAll')
def empregados():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id_empregado, nome_empregado, cpf, sexo, data_nascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais FROM EMPREGADOS")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/getById/<int:idEmpregado>')
def empregado(idEmpregado):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id_empregado, nome_empregado, cpf, sexo, data_nascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais FROM EMPREGADOS WHERE id_empregado=%s", idEmpregado)
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
def update_empregado():
	try:
		_json = request.json
        _id_empregado = _json['id_empregado']
		_nome = _json['nome']
		_cpf = _json['cpf']
        _sexo = _json['sexo']
        _dataNascimento = _json['dataNascimento']
        _telefone = _json['telefone']
        _celular = _json['celular']
        _email = _json['email']
        _endereco = _json['endereco']
        _complemento = _json['complemento']
        _bairro = _json['bairro']
        _cep = _json['cep']
        _cidade = _json['cidade']
        _estado = _json['estado']
        _pais = _json['pais']	

		# validate the received values
		if _id_empregado and request.method == 'PUT':
			
			# save edits
			sql = "UPDATE nome_empregado=%s, cpf=%s, sexo=%s, data_nascimento=%s, telefone=%s, celular=%s, email=%s, endereco=%s, complemento=%s, bairro=%s, cep=%s, cidade=%s, estado=%s, pais=%s FROM EMPREGADOS WHERE id_empregado=%s"
			data = (_nome, _cpf, _sexo, _dataNascimento, _telefone, _celular, _email, _endereco, _complemento, _bairro, _cep, _cidade, _estado, _pais, _id_empregado)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Empregado atualizado com sucesso!')
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
def delete_empregado(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
        sql = "DELETE FROM EMPREGADOS WHERE id_empregado=%s"
		cursor.execute(sql, id)
		conn.commit()
		resp = jsonify('Empregado deletado com sucesso!')
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
		


