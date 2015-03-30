# XXX 
# python encapsulation ?


class test:
    def __init__(self):
    	self.data = {};
    def __setitem__(self,key,item):
    	self.data[key] = item
    def __getitem__(self, key):
    	return self.hasattr(key) and self.data[key] or None
    def hasattr(self,key):
    	return self.data.get(key) and True or False

t = test()
t["a"] = {"test" : 1 }
print t["n"]
print t.hasattr("a")


