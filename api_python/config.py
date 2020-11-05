from app import app
from flaskext.mysql import MySQL

DEBUG = True

mysql = MySQL()

MYSQL_DATABASE_USER = 'reidocangaco'
MYSQL_DATABASE_PASSWORD = 'reidocangaco'
MYSQL_DATABASE_DB = 'reidocangacodb'
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_CHARSET = 'utf8'

<<<<<<< HEAD
=======


>>>>>>> c725f57a97ce60515791897face188ab3662ea59
mysql.init_app(app)



