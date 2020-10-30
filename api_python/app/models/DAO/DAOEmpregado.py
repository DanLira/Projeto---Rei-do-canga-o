from app.models.DAO.tables import Empregado
from app import db

#metodo para salvar um empregado
def salvarEmpregado():
    i = Empregado(
        "Rafael Joaquim",
        "059.045.345-34",
        "M",
        "14/12/1984",
        "64 8888 8888",
        "81 98775 9671",
        "rafaelcybersistemas@gmail.com",
        "rua barão de buique, n 22",
        "Estancia",
        "50771-610",
        "Casa",
        "Recife",
        "PE",
        "Brasil"
        )
    db.session.add(i)
    db.session.commit()
