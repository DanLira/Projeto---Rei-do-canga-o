from app import db

class Empregado(db.Model):
    __tablename__ = "empregados"

    id_empregado = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(14), unique = True)
    sexo = db.Column(db.String(1))
    dataNascimento = db.Column(db.String(10))
    telefone = db.Column(db.String(12))
    celular = db.Column(db.String(20))
    email = db.Column(db.String(120), unique = True)
    endereco = db.Column(db.String(150))
    complemento = db.Column(db.String(70))
    bairro = db.Column(db.String(50))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(2))
    pais = db.Column(db.String(30))
   

    def __init__(self, nome, cpf, sexo, dataNascimento, celular, email, endereco, bairro, cidade, estado, pais):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.dataNascimento = dataNascimento
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __repr__(self):
        return "<Empregado %r>" % self.nome

    
class User(db.Model):
    __tablename__ = "users"
    
    id_user = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    tipo = db.Column(db.String)

    id_empregado = db.Column(db.Integer, db.ForeignKey(empregados.id_empregado))
    empregado = db.relationship('empregados', foreign_keys = id_empregado)

    def __init__(self, username, password, tipo, id_empregado):
        self.username = userName
        self.password = password
        self.tipo = tipo
        self.id_empregado = id_empregado

    def __repr__(self):
        return "<User %r>" % self.username


class FornecedorPF(db.Model):
    __tablename__ = "fornecedorespf"

    id_fornecedorpf = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150))
    nickname = db.Column(db.String(50))
    cpf = db.Column(db.String(14), unique = True)
    sexo = db.Column(db.String(1))
    dataNascimento = db.Column(db.String(10))
    telefone = db.Column(db.String(12))
    celular = db.Column(db.String(20))
    email = db.Column(db.String(120))
    endereco = db.Column(db.String(150))
    complemento = db.Column(db.String(70))
    bairro = db.Column(db.String(50))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(2))
    pais = db.Column(db.String(30))

    def __init__(self, nome, cpf, sexo, dataNascimento, celular, email, endereco, bairro, cidade, estado, pais):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.dataNascimento = dataNascimento
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __repr__(self):
        return "<Fornecedor PF %r>" % self.nome


class FornecedorPJ(db.Model):
    __tablename__ = "fornecedorespj"

    id_fornecedorPJ = db.Column(db.Integer, primary_key = True)
    razaoSocial = db.Column(db.String(150))
    nomeFantasia = db.Column(db.String(150))
    nickname = db.Column(db.String(50))
    cnpj = db.Column(db.String(18))
    telefone = db.Column(db.String(12))
    celular = db.Column(db.String(20))
    email = db.Column(db.String(120))
    endereco = db.Column(db.String(150))
    complemento = db.Column(db.String(70))
    bairro = db.Column(db.String(50))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(2))
    pais = db.Column(db.String(30))

    def __init__(self, razaoSocial, nomeFantasia, cnpj, celular, email, endereco, bairro, cidade, estado, pais):
        self.razaoSocial = razaoSocial
        self.nomeFantasia = nomeFantasia
        self.cnpj = cnpj
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def __repr__(self):
        return "<Fornecedor PJ %r>" % self.nomeFantasia

class Produto(db.Model):
    __tablename__ = "produtos"

    id_produto = db.Column(db.Integer, primary_key = True)
    descProduto = db.Column(db.String(100))
    preco = db.Column(db.String(10))
    tipoVolume = db.Column(db.String(3))

    id_fornecedorpf = db.Column(db.Integer, db.ForeignKey(fornecedorespf.id_fornecedorpf))
    fornecedorpf = db.relationship('fornecedorespf', foreign_keys = id_fornecedorpf)

    id_fornecedorpj = db.Column(db.Integer, db.ForeignKey(forncedorespj.id_fornecedorpj))
    fornecedorpj = db.relationship('fornecedorespj', foreign_keys = id_fornecedorpj)


    def __init__(self, descProduto, preco, tipoVolume):
        self.descProduto = descProduto
        self.preco = preco
        self.tipoVolume = tipoVolume

    def __repr__(self):
        return "<Produto %r>" % self.descProduto

class Pedido(db.Model):
    __tablename____ = "pedidos"

    id_pedido = db.Column(db.Integer, primary_key = True)
    dataPedido = db.Column(db.String(10))
    statusPedido = db.Column(db.String(15))
    valorTotalPedido = db.Column(db.String(15))
    id_usuario = db.Column(db.Integer, db.ForeignKey(usuarios.id_usuario))
    usuario = db.relationship('usuarios', foreign_keys = id_usuario)


    def __init__(self, dataPedido, statusPedido, id_usuario):
        self.dataPedido = dataPedido
        self.statusPedido = statusPedido
        self.id_usuario = id_usuario

class PedidoProduto(db.Model):
    __tablename__ = 'pedidoprodutos'
   
    id_pedido = db.Column(db.Integer, db.ForeignKey(pedidos.id_pedido))
    pedido = db.relationship('pedidos', foreign_keys = id_pedido)
    
    id_produto = db.Column(db.Integer, db.ForeignKey(produtos.id_produto))
    produto = db.relationship('produtos', foreign_keys = id_produto)

    quantidade = db.Column(db.Integer)
    valorTotal = db.Column(db.String(15))

    def __init__(self, id_pedido, id_produto, quantidade, valorTotal):
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.valorTotal = valorTotal


class Venda(db.Model):
    __tablename__ = 'vendas'

    id_venda = db.Column(db.Integer, primary_key = True)
    dataVenda = db.Column(db.String(10))
    statusVenda = db.Column(db.String(15))
    valorTotalVenda = db.Column(db.String(15))

    id_pedido = db.Column(db.Integer, db.ForeignKey(pedidos.id_pedido))
    pedido = db.relationship('pedidos', foreign_keys = id_pedido)



