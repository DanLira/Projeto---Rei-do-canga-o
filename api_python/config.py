# DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://reidocangaco:reidocangaco@localhost/reidocangacodb'

# SQLALCHEMY_TRACK_MODIFICATIONS = True

from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'oreidocangaco'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)