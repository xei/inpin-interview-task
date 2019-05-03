from app import db
from ad import Ad, ad_schema, ads_schema

def create_add(agency_id, name, latitude, longitude):
	'''
	This function creates a new tupple in Ad table.
	return 0 means everything accomplished successfully.
	return 1 means the operation was unsuccessfull.
	'''
	try:
		ad = Ad(agency_id, name, latitude, longitude)
		db.session.add(ad)
		db.session.commit()
		return 0
	except Exception as e:
		print('error while creating the ad: ' + str(e))
		return 1