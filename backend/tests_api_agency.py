import unittest
from app import app, db
from agency import Agency
from agency_controller import *
from ad import Ad

DB_TEST_USER = 'root'
DB_TEST_PASS = '12345678'
DB_TEST_HOST = 'localhost'
DB_TEST_NAME = 'inpin_db'


class AgencyApiTestCase(unittest.TestCase):
	def setup(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False	
		app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_TEST_USER, DB_TEST_PASS, DB_TEST_HOST, DB_TEST_NAME)
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_create_new_agency(self):
		return_code = create_agency('RDHHHGYDK', None)
		agency = Agency.query.filter_by(name='RDHHHGYDK').first()
		db.session.delete(agency)
		db.session.commit()
		self.assertEqual(return_code, 0)

	def test_read_agency(self):
		agency = Agency('FDHUKSDI', None)
		db.session.add(agency)
		db.session.commit()
		agency_name = read_agency(agency.id)['name']
		db.session.delete(agency)
		db.session.commit()
		self.assertEqual(agency_name, 'FDHUKSDI')
		

if __name__ == '__main__':
	unittest.main()