from app import db
from ad import Ad

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

def read_ad(id):
	'''
	This function finds the first tuple with id=id in Ad table,
	serializes it to json and returns the result.
	DECIMAL type is not a serializable type,
	so we could not use Marshmallow here and the json is made manually.
	'''
	try:
		ad = Ad.query.filter_by(id=id).first()
		ad_json = {
			'agency_id' : ad.agency_id,
			'name': ad.name,
			'latitude': float(ad.latitude),
			'longitude': float(ad.longitude)
		}
		return ad_json
	except Exception as e:
		print('error while reading the ad: ' + str(e))
		return None