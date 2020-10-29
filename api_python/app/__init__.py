from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://reidocangaco:reidocangaco@localhost/reidocangacoconexion'
db = SQLAlchemy(app)

from app.controllers import default



