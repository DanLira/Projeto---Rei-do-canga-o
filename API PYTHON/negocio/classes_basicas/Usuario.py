class Usuario(object):

    codUsuario = None
    login = None
    senha = None
    tipo = None
    codUsuInc = None
    datInc = None

    def __init__(self, login, senha, tipo):
        self.login = login
        self.senha = senha
        self.tipo = tipo

    def getCodUsuario(self):
        return self.codUsuariosuario

    def setCodUsuario(self, codUsuario):
        self.codUsuariosuario = codUsuario

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getCodUsuInc(self):
        return self.codUsuInc

    def setCodUsuInc(self, codUsuInc):
        self.codUsuInc = codUsuInc

    def getDatInc(self):
        return self.datInc

    def setDatInc(self, datInc):
        self.datInc = datInc
