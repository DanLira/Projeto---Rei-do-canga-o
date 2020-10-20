from negocio.classes_basicas.ContatoEndereco import ContatoEndereco

class FornecedorPJ(object):

    codFornecedorPJ = None
    razaoSocial = None
    nomeFantasia = None
    nickName = None
    cnpj = None
    codUsuInc = None
    datInc = None

    def __init__(self, razaoSocial, nomeFantasia, cnpj):
        self.razaoSocial = razaoSocial
        self.nomeFantasia = nomeFantasia
        self.cnpj = cnpj

    def getCodFornecedorPJ(self):
        return self.codFornecedorPJ
    def setCodFornecedorPJ(self, codFornecedorPJ):
        self.codFornecedorPJ = codFornecedorPJ

    def getRazaoSocial(self):
        return self.razaoSocial
    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial

    def getNomeFantasia(self):
        return self.nomeFantasia
    def setNomeFantasia(self, nomeFantasia):
        self.nomeFantasia = nomeFantasia

    def getNickName(self):
        return self.nickName
    def setNickName(self, nickName):
        self.nickName = nickName

    def getCnpj(self):
        return self.cnpj
    def setCnpj(self, cnpj):
        self.cnpj = cnpj

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