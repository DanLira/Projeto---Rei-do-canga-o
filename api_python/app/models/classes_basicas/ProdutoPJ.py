class ProdutoPJ(Produto):
    
    id_fornecedorpj = None

     def __init__(self, descProduto, preco, tipoVolume, id_fornecedorpj):
        self.descProduto = descProduto
        self.preco = preco
        self.tipoVolume = tipoVolume
        self.id_fornecedorpj = id_fornecedorpj

    def getIdFornecedorPJ(self):
        return self.id_fornecedorpj

    def setIdFornecedorPJ(self, id_fornecedorpj):
        self.id_fornecedorpj = id_fornecedorpj