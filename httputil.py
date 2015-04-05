# httputil
# @author : SJ
# @date : 2015.03.22
# @purpose : http util class for shodan study

## TO_DO : sending http request asynchronously 
##		   with ip address from config file

import urllib2;
import commonutil;
class Request(urllib2.Request) :

	# url : request url
	# timeout[optional , default = 5second] : request timeout
	# call super class __init__
	def __init__(self, url=None, timeout = 1):
		self.url = url;
		self.timeout = timeout;
		urllib2.Request.__init__(self, url);

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

	def get(self, key, failobj=None):
		return self.__dict__.get(key, failobj)

	def disconnectRequest(self):
		if self.connection : self.connection.close();


class Response:
	
	""" Response class"""

	def __init__(self, connection, sucess = True, url =None):
		self.sucess = sucess;
		self.url = url;
		if connection :
			self.connection = connection;
			self.header = dict((x, y) for x, y in self.connection.info().items());
			self.statusCode = self.connection.getcode();

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

	def __delattr__(self, key):
		del self.__dict__[key]

	def __delitem__(self, key):
		del self.__dict__[key]
		
	def get(self, key, failobj=None):
		return self.__dict__.get(key, failobj)

	# determine success of reqeust on status code
	# if the code is below 400(upper 400, it means fail), it is successed
	# return boolean
	def isSuccess(self):
		# if there is Exception, return false;
		if self.statusCode <400 :
			return True;
		else :
			return False;

	# To figure out which server is used in web site
	# return : server name

	## TO_DO : logic to determin server name

	def getServerInfo(self):
		self.server="";

		if not self.connection:
			print "connection fail"
			return None

		# ServerInfo
		# first find out "x-powered-by" field from response header
		if self.header.get("x-powered-by"):
			temp =self.header.get("x-powered-by").lower();

			# if there is "x-powered-by" field then find out server name
			# add different server name logic from here
			if temp.find("JBoss".lower()) > 0:
				self.server = "JBoss";
			elif temp.find("Tomcat".lower()) > 0:
				self.server = "Tomcat";
			else :
				self.server = self.header.get("x-powered-by");
		elif self.header.get("server"):
			self.server = self.header.get("server");
		return self.server;

	def setErrorInfo(self, e):
		if hasattr(e, "code") :
			self.statusCode = e.code;
		else: 
			self.statusCode = 404;
		if hasattr(e, "headers") :
			self.header = e.headers;
		if hasattr(e, "args") and len(e.args) > 0 :
			self.errorMessage = e.args[0];

		print "[HTTP ERROR] : %s >> %s" % (self.url , self.errorMessage);

# @purpose : http request and get response
# @param : request [urllib2 obj]
#		 , timeout [ second]
#		 , data [ request data] 
def httpRequest(request , timeout =2 ,data=None):

	connection = None;

	if request.get_full_url().find("http://") :
		raise Exception("Wrong Url [URL should be started with 'http://' ]");
	try :
		connection = urllib2.urlopen(request ,data ,timeout);
	except Exception, e:
		response= Response(None, False, request.get_full_url());
		response.setErrorInfo(e);
		return response;

	response = Response(connection);
	response.url = request.get_full_url();

	return response;	


# read config file and try login based on userInfo from config file
# return response obj(httputil)	
def server_opener(response):
	serverName = response.getServerInfo();
	if not serverName:
		return serverName

	## TO_DO : adding url based on different WAS
	if serverName.lower() == "tomcat" :
		suffix = "manager/";
	else :
		suffix = "manager/";

	## making WAS manager url
	if response.url[-1] == "/" :
		url = response.url + suffix;
	else : 
		url = response.url + "/" +suffix;

	## copy python authentication sample
	pwList = commonutil.getPasswordList().get(serverName);

	if not pwList :
		pwList = {}
		pwList["admin"] = "admin"

	passman = urllib2.HTTPPasswordMgrWithDefaultRealm();
	## add passwd list from config file
	for key in pwList.keys():
		passman.add_password(None, url , key, pwList.get(key));
	authhandler = urllib2.HTTPBasicAuthHandler(passman);
	opener = urllib2.build_opener(authhandler);
	urllib2.install_opener(opener);
	req = Request(url);

	# convert httputil response obj and return it
	return httpRequest(req);


