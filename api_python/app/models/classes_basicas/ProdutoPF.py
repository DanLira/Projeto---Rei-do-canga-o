class ProdutoPF(Produto):
    
    id_fornecedorpf = None

    def __init__(self, descProduto, preco, tipoVolume, id_fornecedorpf):
        self.descProduto = descProduto
        self.preco = preco
        self.tipoVolume = tipoVolume
        self.id_fornecedorpf = id_fornecedorpf

    def getIdFornecedorPF(self):
        return self.id_fornecedorpf

    def setIdFornecedorPF(self, id_fornecedorpf):
        self.id_fornecedorpf = id_fornecedorpf