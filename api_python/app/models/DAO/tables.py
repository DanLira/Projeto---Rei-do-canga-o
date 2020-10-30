from app import db

class Empregado(db.Model):
    __tablename__ = "empregados"

    id_empregado = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(14), unique = True, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    dataNascimento = db.Column(db.String(10), nullable=False)
    telefone = db.Column(db.String(12))
    celular = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(70))
    bairro = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    pais = db.Column(db.String(30), nullable=False)
   

    def __init__(self, nome, cpf, sexo, dataNascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.endereco = endereco
        self.bairro = bairro
        self.cep = cep
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    
class User(db.Model):
    __tablename__ = "users"
    
    id_user = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(15), nullable=False)

    id_empregado = db.Column(db.Integer, db.ForeignKey(Empregado.id_empregado), nullable=False)
    empregado = db.relationship('empregados', foreign_keys = id_empregado)

    def __init__(self, username, password, tipo, id_empregado):
        self.username = userName
        self.password = password
        self.tipo = tipo
        self.id_empregado = id_empregado


class FornecedorPF(db.Model):
    __tablename__ = "fornecedorespf"

    id_fornecedorpf = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(150), nullable=False)
    nickname = db.Column(db.String(50))
    cpf = db.Column(db.String(14), unique = True, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    dataNascimento = db.Column(db.String(10))
    telefone = db.Column(db.String(12))
    celular = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(70))
    bairro = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    pais = db.Column(db.String(30), nullable=False)

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



class FornecedorPJ(db.Model):
    __tablename__ = "fornecedorespj"

    id_fornecedorpj = db.Column(db.Integer, primary_key = True, autoincrement = True)
    razaoSocial = db.Column(db.String(150), nullable=False)
    nomeFantasia = db.Column(db.String(150), nullable=False)
    nickname = db.Column(db.String(50))
    cnpj = db.Column(db.String(18), nullable=False)
    telefone = db.Column(db.String(12))
    celular = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    endereco = db.Column(db.String(150), nullable=False)
    complemento = db.Column(db.String(70))
    bairro = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    pais = db.Column(db.String(30), nullable=False)

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



class Produto(db.Model):
    __tablename__ = "produtos"

    id_produto = db.Column(db.Integer, primary_key = True, autoincrement = True)
    descProduto = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(10), nullable=False)
    tipoVolume = db.Column(db.String(2), nullable=False)

    id_fornecedorpf = db.Column(db.Integer, db.ForeignKey(FornecedorPF.id_fornecedorpf))
    fornecedorpf = db.relationship('fornecedorespf', foreign_keys = id_fornecedorpf)

    id_fornecedorpj = db.Column(db.Integer, db.ForeignKey(FornecedorPJ.id_fornecedorpj))
    fornecedorpj = db.relationship('fornecedorespj', foreign_keys = id_fornecedorpj)


    def __init__(self, descProduto, preco, tipoVolume):
        self.descProduto = descProduto
        self.preco = preco
        self.tipoVolume = tipoVolume


class Pedido(db.Model):
    __tablename____ = "pedidos"

    id_pedido = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dataPedido = db.Column(db.String(10), nullable=False)
    statusPedido = db.Column(db.String(15), nullable=False)
    valorTotalPedido = db.Column(db.String(15))
    id_usuario = db.Column(db.Integer, db.ForeignKey(User.id_user), nullable=False)
    usuario = db.relationship('usuarios', foreign_keys = id_usuario)


    def __init__(self, dataPedido, statusPedido, id_usuario):
        self.dataPedido = dataPedido
        self.statusPedido = statusPedido
        self.id_usuario = id_usuario


        
class PedidoProduto(db.Model):
    __tablename__ = 'pedidoprodutos'
   
    id_pedido = db.Column(db.Integer, db.ForeignKey(Pedido.id_pedido), primary_key=True, nullable=False)
    pedido = db.relationship('pedidos', foreign_keys = id_pedido)
    
    id_produto = db.Column(db.Integer, db.ForeignKey(Produto.id_produto), primary_key=True, nullable=False)
    produto = db.relationship('produtos', foreign_keys = id_produto)

    quantidadeProduto = db.Column(db.Integer, nullable=False)
    valorTotal = db.Column(db.String(15), nullable=False)

    def __init__(self, id_pedido, id_produto, quantidadeProduto, valorTotal):
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidadeProduto = quantidadeProduto
        self.valorTotal = valorTotal



class Venda(db.Model):
    __tablename__ = 'vendas'

    id_venda = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dataVenda = db.Column(db.String(10), nullable=False)
    statusVenda = db.Column(db.String(15), nullable=False)
    valorTotalVenda = db.Column(db.String(15), nullable=False)

    id_pedido = db.Column(db.Integer, db.ForeignKey(Pedido.id_pedido), nullable=False)
    pedido = db.relationship('pedidos', foreign_keys = id_pedido)

    def __init__(self, dataVenda, statusVenda, valorTotalVenda):
        self.dataVenda = dataVenda
        self.statusVenda = statusVenda
        self.valorTotalVenda = valorTotalVenda


db.create_all()
