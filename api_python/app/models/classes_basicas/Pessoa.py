from app.models.classes_basicas.ContatoEndereco import ContatoEndereco

class Pessoa(object):

    nome = None
    nickName = None
    cpf = None
    sexo = None
    dataNascimento = None


    def __init__(self, nome, cpf, sexo, dataNascimento):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.dataNascimento = dataNascimento

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

    def getDataNascimento(self):
        return self.dataNascimento

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento


    class ContatoEndereco(ContatoEndereco):
        pass