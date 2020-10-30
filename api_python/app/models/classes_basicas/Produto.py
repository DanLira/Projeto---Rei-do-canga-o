class Produto(object):

    id_produto = None
    descProduto = None
    preco = None
    tipoVolume = None
 
    def getId_produto(self):
        return self.id_produto

    def setId_produto(self, id_produto):
        self.id_produto = id_produto

    def getdescProduto(self):
        return self.descProduto

    def setDescProduto(self, descProduto):
        self.descProduto = descProduto

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
    
    def getTipoVolume(self):
        return self.tipoVolume

    def setTipoVolume(self, tipoVolume):
        self.tipoVolume = tipoVolume

