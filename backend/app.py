from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

DB_USER = 'root'
DB_PASS = '12345678'
DB_HOST = 'localhost'
DB_NAME = 'inpin_db'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)