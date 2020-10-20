from negocio.classes_basicas.Pessoa import Pessoa

class Vendedor(Pessoa):

    codVendedor = None
    dataNascimento = None

    def getCodVendedor(self):
        return self.codVendedor

    def setCodVendedor(self, codVendedor):
        self.codVendedor = codVendedor

    def getDataNascimento(self):
        return self.dataNascimento

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento
