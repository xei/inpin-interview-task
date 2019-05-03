from app import app
from flask import jsonify, request
import agency_controller
import ad_controller


@app.route('/agency', defaults={'id': None}, methods=['GET', 'POST'])
@app.route('/agency/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def agency_view(id):
	'''
	This function is an entry point for the endpoint "/agency" and
	handle GET, POST, PUT and DELETE http requests.
	'''
	if request.method == 'GET':

		if id != None:
			return jsonify(read_agency(id))
		else:
			return jsonify(read_all_agencies())

	elif request.method == 'POST':

		parent_id = None
		try:
			parent_id = request.form['parent_id']
		except Exception as e:
			# The agency should be root (parent_id = None)
			pass
		try:
			name = request.form['name']
			if create_agency(name, parent_id) == 0:
				return jsonify(make_msg_response(True, 'Agency created successfully.'))
			else:
				return jsonify(make_msg_response(False, 'Agency did not created successfully.'))
		except Exception as e:
			return jsonify(make_msg_response(False, 'This API needs a name for agency'))

	elif request.method == 'PUT':

		try:
			new_name = request.form['name']
			new_parent_id = request.form['parent_id']
			if update_agency(id, new_name, new_parent_id) == 0:
				return jsonify(make_msg_response(True, 'Agency updated successfully.'))
			else:
				return jsonify(make_msg_response(False, 'Agency did not update successfully.'))
		except Exception as e:
			return jsonify(make_msg_response(False, 'This API needs new name and parent_id'))

	elif request.method == 'DELETE':

		if delete_agency(id) == 0:
			return jsonify(make_msg_response(True, 'Agency deleted successfully.'))
		else:
			return jsonify(make_msg_response(False, 'Agency did not delete successfully.'))

	else:
		# 404
		pass

@app.route('/ad', defaults={'id': None}, methods=['GET', 'POST'])
@app.route('/ad/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def ad_view(id):
	'''
	This function is an entry point for the endpoint "/agency" and
	handle GET, POST, PUT and DELETE http requests.
	'''
	if request.method == 'GET':

		if id != None:
			return jsonify(read_ad(id))
		else:
			try:
				agency_id = request.args['agency']
				show_sub_agencies_ads = False # Default value for argument 'sub'
				try:
					sub = request.args['sub']
					show_sub_agencies_ads = (sub.lower() == 'true')
				except Exception as e:
					# argument 'sub' is not provided.
					# so use it's default value (False)
					pass
				return jsonify(read_agency_ads(agency_id, list_sub_agencies_ads))
			except Exception as e:
				# argument 'agency' is not provided
				# so the response should be independant from any agencies.
				try:
					latitude = float(request.args['lat'])
					longitude = float(request.args['lon'])
					distance = float(request.args['dist'])
					return jsonify(read_near_ads(latitude, longitude, distance))
				except Exception as e:
					# geographic arguments are not completed
					# so we should list all the ads.
					return jsonify(read_all_ads())
			
	elif request.method == 'POST':

		try:
			agency_id = request.form['agency_id']
			name = request.form['name']
			latitude = request.form['latitude']
			longitude = request.form['longitude']
			if create_ad(agency_id, name, latitude, longitude) == 0:
				return jsonify(make_msg_response(True, 'Ad created successfully.'))
			else:
				return jsonify(make_msg_response(False, 'Ad did not created successfully.'))
		except Exception as e:
			return jsonify(make_msg_response(False, 'This API needs some information for ad'))

	elif request.method == 'PUT':

		try:
			new_agency_id = request.form['agency_id']
			new_name = request.form['name']
			new_latitude = request.form['latitude']
			new_longitude = request.form['longitude']
			if update_ad(id, new_agency_id, new_name, new_latitude, new_longitude) == 0:
				return jsonify(make_msg_response(True, 'Ad updated successfully.'))
			else:
				return jsonify(make_msg_response(False, 'Ad did not update successfully.'))
		except Exception as e:
			return jsonify(make_msg_response(False, 'This API needs new agency_id, name, latitude and longitude'))

	elif request.method == 'DELETE':

		if delete_ad(id) == 0:
			return jsonify(make_msg_response(True, 'Ad deleted successfully.'))
		else:
			return jsonify(make_msg_response(False, 'Ad did not delete successfully.'))

	else:
		# 404
		pass

def make_msg_response(succeed, msg):
	'''
	This function returns a wrapper Json object as a
	successful/unsuccessful mesage to client app.
	'''
	return {
		'status' : bool(succeed),
		'msg' : msg
	}

if __name__ == "__main__":
    app.run()