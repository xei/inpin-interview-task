from sqlalchemy import create_engine
from app import DB_USER, DB_PASS, DB_HOST, DB_NAME, db
from agency import Agency
from ad import Ad

# Connect to database server
db_uri = 'mysql+pymysql://{}:{}@{}'.format(DB_USER, DB_PASS, DB_HOST)
engine = create_engine(db_uri)

# Create Database
query_create_db = 'CREATE DATABASE IF NOT EXISTS {} ;'.format(DB_NAME)
engine.execute(query_create_db)

# Create tables
db.create_all()