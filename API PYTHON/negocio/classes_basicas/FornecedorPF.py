from negocio.classes_basicas.Pessoa import Pessoa

class FornecedorPF(Pessoa):

    codFornecedorPF = None

    def getCodFornecedorPF(self):
        return self.codFornecedorPF
    def setCodFornecedorPF(self, codFornecedorPF):
        self.codFornecedorPF = codFornecedorPF


