from app import db
from ad import Ad
from agency_controller import all_found_agencies, find_sub_agencies

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

def read_all_ads():
	'''
	This function reads, serializes and returns all the tupples in Ad table.
	'''
	try:
		ads = Ad.query.all()
		ads_json = [{
			'agency_id' : ad.agency_id,
			'name': ad.name,
			'latitude': float(ad.latitude),
			'longitude': float(ad.longitude)
		} for ad in ads]
		return ads_json
	except Exception as e:
		print('error while reading all ads: ' + str(e))
		return None

def read_agency_ads(agency_id, show_sub_agencies_ads):
	'''
	This function reads, serializes and returns all tupples in Ad table that
	belongs to a distinct agency (and it's sub-agencies
	based on the bool variable show_sub_agencies_ads)
	'''
	try:
		if show_sub_agencies_ads:
			all_found_agencies.clear()
			find_sub_agencies(int(agency_id))
			ads = Ad.query.filter(Ad.agency_id.in_(all_found_agencies)).all()
			ads_json = [{
				'agency_id' : ad.agency_id,
				'name': ad.name,
				'latitude': float(ad.latitude),
				'longitude': float(ad.longitude)
			} for ad in ads]
			return ads_json
		else:
			ads = Ad.query.filter_by(agency_id=agency_id).all()
			ads_json = [{
				'agency_id' : ad.agency_id,
				'name': ad.name,
				'latitude': float(ad.latitude),
				'longitude': float(ad.longitude)
			} for ad in ads]
		return ads_json
	except Exception as e:
		print('error while reading agency ads: ' + str(e))
		return None

def read_near_ads(latitude, longitude, distance):
	'''
	This function reads, serializes and returns all tupples in Ad table that
	their geographical location is nearer than distance (Killometer) in order.
	Instead of using GIS database extensions, SqlAlchemy Hybrid method and Great Circle
	formula are used here to query the database for calculating the distances.
	'''
	try:
		ads = db.session.query(
        	Ad,
        	Ad.distance(latitude, longitude).label('distance'),
        	Ad.agency_id,
        	Ad.name,
        	Ad.latitude,
        	Ad.longitude
    	).having(db.column('distance') <= distance)
    	.order_by('distance')
    	.all()
		ads_json = [{
			'agency_id' : ad.agency_id,
			'name': ad.name,
			'latitude': float(ad.latitude),
			'longitude': float(ad.longitude),
			'distance': ad.distance
		} for ad in ads]
		return ads_json
	except Exception as e:
		print('error while reading near ads: ' + str(e))
		return None

def update_ad(id, new_agency_id, new_name, new_latitude, new_longitude):
	'''
	This function finds the first tupple with id=id in Ad table
	and update it's columns.
	return 0 means everything accomplished successfully.
	return 1 means the operation was unsuccessfull.
	'''
	try:
		ad = Ad.query.filter_by(id=id).first()
		ad.agency_id = new_agency_id
		ad.name = new_name
		ad.latitude = new_latitude
		ad.longitude = new_longitude
		db.session.commit()
		return 0
	except Exception as e:
		print('error while updating the ad: ' + str(e))
		return 1