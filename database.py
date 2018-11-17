import pickle

class Database(object):
	def __init__(self):
		self.data = {}

	def save(self, filename):
		print('saving to', filename)
		with open(filename, 'wb') as file:
			pickle.dump(self.data, file)


	def load(self, filename):
		print('loading from', filename)
		try:
			with open(filename, 'rb') as file:
				self.data = pickle.load(file)
		except FileNotFoundError:
			self.data = {}