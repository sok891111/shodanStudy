import copy

class test:
	def __init__(self):
		pass
	def __contains__(self, key):
		return key in self.__dict__
	def __delitem__(self, key):
		del self.__dict__[key]
	# getter 메소드
	def __getattr__(self, key):
		return hasattr(self, key) and self.__dict__[key] or None
	# setter 메소드
	def __setattr__(self, key ,value):
		self.__dict__[key] = value
	def copy(self):
		return copy.deepcopy(self)
	def get(self, key, failobj=None):
		return self.__dict__.get(key, failobj)
	
	def __str__(self):
		return str(self.__dict__)
	def __len__(self):
		return len(self.__dict__)
