from negocio.classes_basicas.ContatoEndereco import ContatoEndereco

class FornecedorPJ(object):

    id_fornecedorpj = None
    razaoSocial = None
    nomeFantasia = None
    nickName = None
    cnpj = None

    def __init__(self, razaoSocial, nomeFantasia, cnpj):
        self.razaoSocial = razaoSocial
        self.nomeFantasia = nomeFantasia
        self.cnpj = cnpj

    def getIdFornecedorPJ(self):
        return self.id_fornecedorpj
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


    class ContatoEndereco(ContatoEndereco):
        pass