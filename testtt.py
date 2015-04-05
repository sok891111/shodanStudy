class Request() :

	# url : request url
	# timeout[optional , default = 5second] : request timeout
	# call super class __init__
	def __init__(self, url=None, timeout = 1):
		self.url = url;
		self.timeout = timeout;

	""" Request class"""
	def __getattr__(self, key):
		try:
			return self.__dict__[key]
		except Exception , e:
			return None

	def __getattribute__(self, name):
		print "test"

	def __getitem__(self, key):
		try:
			return self.__dict__[key]
		except Exception , e:
			return None

	def __setattr__(self, key ,value):
		self.__dict__[key] = value

	def __setitem__(self, key, value):
		self.__dict__[key] = value

	def get(self, key, failobj=None):
		return self.__dict__.get(key, failobj)

	def disconnectRequest(self):
		if self.connection : self.connection.close();
	def __delattr__(self, key):
		del self.__dict__[key]

t = Request("www.naver.com" , 2);
t.url = "test"
t["url"] = "asdf"
del t.url
print t.url