sessions = {}

def get_session(id):
	try:
		return sessions[id]
	except KeyError:
		return None

def add_session(id, data):
	sessions[id] = data