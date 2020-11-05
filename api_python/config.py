from app import app
from flaskext.mysql import MySQL

DEBUG = True

mysql = MySQL()

MYSQL_DATABASE_USER = 'reidocangaco'
MYSQL_DATABASE_PASSWORD = 'reidocangaco'
MYSQL_DATABASE_DB = 'reidocangacodb'
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_CHARSET = 'utf8'

mysql.connect(host = MYSQL_DATABASE_HOST, user = MYSQL_DATABASE_USER, passwd = MYSQL_DATABASE_PASSWORD, db = MYSQL_DATABASE_DB)

mysql.init_app(app)





