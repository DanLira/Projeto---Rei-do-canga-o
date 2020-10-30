class Pedido(object):

    id_pedido = None
    datPedido = None
    statusPedido = None
    id_usuario = None

    def __init__(self, datPedido, statusPedido, codVendedor):
        self.datPedido = datPedido
        self.statusPedido = statusPedido
        self.codVendedor = codVendedor

    def getIdPedido(self):
        return self.id_pedido

    def setIdPedido(self, id_pedido):
        self.id_pedido = id_pedido

    
    def getDatPedido(self):
        return self.datPedido

    def setDatPedido(self, datPedido):
        self.datPedido = datPedido

    
    def getStatusPedido(self):
        return self.statusPedido

    def setStatusPedido(self, statusPedido):
        self.statusPedido = statusPedido

    
    def getIdUsuario(self):
        return self.id_usuario

    def setIdUsuario(self, id_usuario):
        self.id_usuario = id_usuario  