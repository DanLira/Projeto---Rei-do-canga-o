from app.models.classes_basicas.Pessoa import Pessoa

class Empregado(Pessoa):

    id_empregado = None
    
    def getEmpregado(self):
        return self.id_empregado

    def setIdEmpregado(self, id_empregado):
        self.id_empregado = id_empregado