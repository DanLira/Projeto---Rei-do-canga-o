from app.models.DAO import DAOUsuario
from app import app

@app.route('/user')
def contrllerAction():

    def add_user():
        return DAOUsuario.add_user()
        
    @app.route('/getAll')
    def users():
        return DAOUsuario.users()


    def user(id):
        return DAOUsuario.user(id)

    def update_user():
        return DAOUsuario.update_user()   

    def delete_user(id):
        return DAOUsuario.delete_user(id)