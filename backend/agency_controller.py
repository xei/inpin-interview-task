# from app import app
from app import db
# from flask import jsonify, request
from agency import Agency, agency_schema, agencies_schema
# from ad import Ad, ad_schema, ads_schema

def create_agency(name, parent_id):
	'''
	This function creates a new tupple in Agency table.
	'''
	agency = Agency(name, parent_id)
	db.session.add(agency)
	db.session.commit()

def read_agency(id):
	'''
	This function finds the first tuple with id=id in Agency table,
	serializes it to json and returns the result.
	'''
	agency = Agency.query.filter_by(id=id).first()
	result = agency_schema.dump(agency)
	return result.data