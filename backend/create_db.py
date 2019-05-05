from app import db
from agency import Agency
from ad import Ad

db.drop_all()
db.create_all()