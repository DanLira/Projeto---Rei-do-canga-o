DEBUG = True

mysql = MySQL()

MYSQL_DATABASE_USER = 'reidocangaco'
MYSQL_DATABASE_PASSWORD = 'reidocangaco'
MYSQL_DATABASE_DB = 'reidocangacodb'
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_CHARSET = 'utf8'

mysqlconfig = (host = MYSQL_DATABASE_HOST, user = MYSQL_DATABASE_USER, password = MYSQL_DATABASE_PASSWORD, database = MYSQL_DATABASE_DB, charset = MYSQL_DATABASE_CHARSET)


mysql.init_app(app)



