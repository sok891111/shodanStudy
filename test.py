import copy

class test:
	def __init__(self):
		self.data = {};
	def __setitem__(self,key,item):
		self.data[key] = item
	def __getitem__(self, key):
		return self.hasattr(key) and self.data[key] or None
	def __contains__(self, key):
		return key in self.data
	def __delitem__(self, key):
		del self.data[key]
	def copy(self):
		return copy.deepcopy(self)
	def get(self, key, failobj=None):
		return self.data.get(key, failobj)
	def hasattr(self,key):
		return key in self.data


t = test()
t["a"] = {"test" : 1 }

b = t.copy()
b["a"] = 1
del b["a"]
print t.hasattr("a")
print t["a"]
print b["a"]
print t.get("n" , "test")
print t.get("a")
