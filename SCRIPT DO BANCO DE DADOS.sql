CREATE DATABASE reidocangacodb

USE reidocangacodb

CREATE TABLE USUARIO (
	cod_usuario int auto_increment primary key,
    login varchar(50) not null, 
    senha varchar(20) not null,
    tipo varchar(30) not null,
    cod_usu_inc int not null,
    dat_inc char(10) not null
)
SELECT * FROM USUARIO
INSERT INTO USUARIO (login, senha, tipo, cod_usu_inc, dat_inc)
VALUES              ("Administrador", "adm123", "Administrador", 1000, "20/10/2020")

#ALTER TABLE USUARIO AUTO_INCREMENT = 1000
#ALTER TABLE FORNECEDORPF AUTO_INCREMENT = 10000
#ALTER TABLE FORNECEDORPJ AUTO_INCREMENT = 100000
#ALTER TABLE PRODUTO AUTO_INCREMENT = 100
#ALTER TABLE VENDEDOR AUTO_INCREMENT = 1000

CREATE TABLE FORNECEDORPF(
	cod_fornecedorpf int auto_increment primary key,
    nome varchar(100) not null,
    nickname varchar(40) null,
    cpf char(14) not null,
    sexo char(1) not null,
    telefone char(12) null,
    celular varchar(20) not null,
    email varchar(80) not null,
    endereco varchar(50) not null,
    complemento varchar(50) null,
    bairro varchar(50) not null,
    cep char(10) null, 
    cidade varchar(50) not null,
    estado char(2) not null,
    pais varchar(30) not null,
    cod_usu_inc int not null,
    dat_inc char(10) not null,
    CONSTRAINT fk_cod_usu_inc_fpf FOREIGN KEY (cod_usu_inc) REFERENCES USUARIO(cod_usuario)
)
CREATE TABLE FORNECEDORPJ(
	cod_fornecedorpj int auto_increment primary key,
    razao_social varchar(100) not null,
    nome_fantasia varchar(100) not null,
    nickname varchar(40) null,
    cnpj char(18) not null,
    telefone char(12) null,
    celular varchar(20) not null,
    email varchar(80) not null,
    endereco varchar(50) not null,
    complemento varchar(50) null,
    bairro varchar(50) not null,
    cep char(10) null, 
    cidade varchar(50) not null,
    estado char(2) not null,
    pais varchar(30) not null,
    cod_usu_inc int not null,
    dat_inc char(10) not null,
    CONSTRAINT fk_cod_usu_inc_fpj FOREIGN KEY (cod_usu_inc) REFERENCES USUARIO(cod_usuario)
)

CREATE TABLE UNIDADE_MEDIDA (
	cod_unidade_medida int auto_increment primary key,
    sigla_unidade_medida varchar(5) not null,
    nome_unidade_medida varchar(20) not null
)

CREATE TABLE PRODUTO(
	cod_produto int auto_increment primary key,
    desc_produto varchar(80) not null,
    desc_abrev_produto varchar(50) null,
    preco decimal(10,2) not null,
    cod_uni_med_compra int null, 
    cod_uni_med_venda int null,  
    cod_tipo_volume int not null,
    cod_fornecedorpj int null,
    cod_fornecedorpf int null,
    cod_usu_inc int not null,
    dat_inc char(10) not null,
    CONSTRAINT fk_cod_uni_med_compra_prod FOREIGN KEY (cod_uni_med_compra) REFERENCES UNIDADE_MEDIDA(cod_unidade_medida),
    CONSTRAINT fk_cod_uni_med_venda_prod FOREIGN KEY (cod_uni_med_venda) REFERENCES UNIDADE_MEDIDA(cod_unidade_medida),
    CONSTRAINT fk_cod_tipo_volume_prod  FOREIGN KEY (cod_tipo_volume) REFERENCES UNIDADE_MEDIDA(cod_unidade_medida),
    CONSTRAINT fk_cod_fornecedorpj_prod  FOREIGN KEY (cod_fornecedorpj) REFERENCES FORNECEDORPJ(cod_fornecedorpj),
    CONSTRAINT fk_cod_fornecedorpf_prod  FOREIGN KEY (cod_fornecedorpf) REFERENCES FORNECEDORPF(cod_fornecedorpf),
    CONSTRAINT fk_cod_usu_inc_prod FOREIGN KEY (cod_usu_inc) REFERENCES USUARIO(cod_usuario)
)

CREATE TABLE FORNECEDORPF_PRODUTO(
	cod_fornecedorpf int not null,
    cod_produto int not null,
    CONSTRAINT fk_cod_fornecedorpf_fornecpfprod FOREIGN KEY (cod_fornecedorpf) REFERENCES FORNECEDORPF(cod_fornecedorpf),
    CONSTRAINT fk_cod_produto_fornecpfprod FOREIGN KEY (cod_produto) REFERENCES PRODUTO(cod_produto)
)

CREATE TABLE FORNECEDORPJ_PRODUTO(
	cod_fornecedorpj int not null,
    cod_produto int not null,
    CONSTRAINT fk_cod_fornecedorpj_fornecpjprod FOREIGN KEY (cod_fornecedorpj) REFERENCES FORNECEDORPJ(cod_fornecedorpj),
    CONSTRAINT fk_cod_produto_fornecpjprod FOREIGN KEY (cod_produto) REFERENCES PRODUTO(cod_produto)
)

CREATE TABLE VENDEDOR(
	cod_vendedor int auto_increment primary key,
    nome_vendedor varchar(100) not null,
    cpf char(14) not null,
    sexo char(1) not null,
    data_nascimento char(10) not null,
    telefone char(12) null,
    celular varchar(20) not null,
    email varchar(80) not null,
    endereco varchar(50) not null,
    complemento varchar(50) null,
    bairro varchar(50) not null,
    cep char(10) null, 
    cidade varchar(50) not null,
    estado char(2) not null,
    pais varchar(30) not null,
    cod_usu_inc int not null,
    dat_inc char(10) not null,
    CONSTRAINT fk_cod_usu_inc_vendedor FOREIGN KEY (cod_usu_inc) REFERENCES USUARIO(cod_usuario)
)
INSERT INTO VENDEDOR (nome_vendedor, cpf, sexo, data_nascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, cod_usu_inc, dat_inc)
VALUES               ('Teste nome vendedor', '059.945.345-34', 'M', '14/12/1995','5545672345', '55 81 98775 9874', 'emailteste', 'rua b, n22', 't comple', 'estancia', '50771-495', 'recife', 'PE', 'brasil', 1000, '20/10/2020')

CREATE TABLE PEDIDO(
	cod_pedido int auto_increment primary key,
    data_pedido char(10) not null,
    status_pedido varchar(15) not null default 'Aberto',
    cod_vendedor int not null,
    CONSTRAINT fk_cod_vendedor_pedido FOREIGN KEY (cod_vendedor) REFERENCES VENDEDOR(cod_vendedor)
)

CREATE TABLE PEDIDO_PRODUTO(
	cod_pedido int not null,
    quantidade_produto int not null,
    cod_produto int not null,
    CONSTRAINT fk_cod_pedido_pedidoproduto FOREIGN KEY (cod_pedido) REFERENCES PEDIDO(cod_pedido),
    CONSTRAINT fk_cod_produto_pedidoproduto FOREIGN KEY (cod_produto) REFERENCES PRODUTO(cod_produto)
)

CREATE TABLE VENDA(
	cod_venda int auto_increment primary key,
    data_venda char(10) not null,
    cod_pedido int not null,
    valor_total_venda decimal(15,2) not null,
    status_venda varchar(15) not null default 'A Receber',
    CONSTRAINT fk_cod_pedido_venda FOREIGN KEY (cod_pedido) REFERENCES PEDIDO(cod_pedido)
)