from app import app
import agency_controller
from flask import jsonify, request


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
				return jsonify(make_msg_response(True, 'Agency did not update successfully.'))
		except Exception as e:
			return jsonify(make_msg_response(False, 'This API needs new name and parent_id'))

	elif request.method == 'DELETE':

		if delete_agency(id) == 0:
			return jsonify(make_msg_response(True, 'Agency deleted successfully.'))
		else:
			return jsonify(make_msg_response(True, 'Agency did not delete successfully.'))

	else:
		# 404
		pass

def make_msg_response(succeed, msg):
	'''
	This function returns a wrapper Json object as a
	successful/unsuccessful mesage to client app.
	'''
	return {
		'status' : bool(succeed)
		'msg' : msg
	}

if __name__ == "__main__":
    app.run()