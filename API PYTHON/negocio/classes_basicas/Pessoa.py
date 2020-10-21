from negocio.classes_basicas.ContatoEndereco import ContatoEndereco

class Pessoa(object):

    nome = None
    nickName = None
    cpf = None
    sexo = None
    codUsuInc = None
    datInc = None

    def __init__(self, nome, cpf, sexo):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getNickName(self):
        return self.nickName

    def setNickName(self, nickName):
        self.nickName = nickName

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getSexo(self):
        return self.sexo

    def setSexo(self, sexo):
        self.sexo = sexo

    def getCodUsuInc(self):
        return self.codUsuInc

    def setCodUsuInc(self, codUsuInc):
        self.codUsuInc = codUsuInc

    def getDatInc(self):
        return self.datInc

    def setDatInc(self, datInc):
        self.datInc = datInc

    class ContatoEndereco(ContatoEndereco):
        pass
