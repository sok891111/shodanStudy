# ResponseUtil
# @author : SJ
# @date : 2015.03.22
# @purpose : response util class for shodan study

import urllib2;

class Request(urllib2.Request) :

	""" Request class"""

	# url : request url
	# timeout[optional , default = 5second] : request timeout
	# call super class __init__
	def __init__(self, url=None, timeout = 1):
		self.url = url;
		self.timeout = timeout;
		urllib2.Request.__init__(self, url);
	# from : request start Ip [e.g 100.100.220.1]
	# to[optional] : request end Ip [e.g 100.100.220.99]
	# timeout[optional , default = 5second] : request timeout

	# def __init__(self, fromIp, toIp , timeout = 5):
	# 	self.fromIp = fromIp;
	# 	if not toIp : toIp = fromIp;
	# 	self.to = to;
	# 	self.timeout = timeout;

	def setUrl(self, url):
		self.url = url;

	def setTimeout(self, timeout):
		self.timeout = timeout;

	def setHeader(self, header):
		self.header = header;

	def disconnectRequest(self):
		if self.connection : self.connection.close();

class Response:
	
	""" Response class"""

	def __init__(self, connection, sucess = True):
		self.sucess = sucess;
		if connection :
			self.connection = connection;
			self.header = dict((x, y) for x, y in self.connection.info().items());
			self.statusCode = self.connection.getcode();

	# return : url
	def getUrl(self):
		return self.connection.get_full_url();

	# return : headerInfo *dictionary
	def getHeader(self):
		return self.header;

	# get response status code
	# return : status code *int
	def getStatusCode(self):
		return self.statusCode;

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
	def getServerInfo(self):
		self.server="";
		# ServerInfo
		# first find out "x-powered-by" field from response header
		if self.header.get("x-powered-by"):
			temp =self.header.get("x-powered-by").lower();

			# if there is "x-powered-by" field then find out server name
			# add different server name logic from here
			if temp.find("JBoss".lower()) > 0:
				self.server = "JBoss";
			elif temp.find("Php".lower()) > 0:
				self.server = "PHP";
			elif temp.find("Tomcat".lower()) > 0:
				self.server = "Tomcat";
			else :
				self.server = self.header.get("x-powered-by");
		elif self.header.get("server"):
			self.server = self.header.get("server");
		return self.server;


	def setStatusCode(self, statusCode) :
		self.statusCode = statusCode;


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
	except Exception as e:
		response= Response(None, False);
		response.setStatusCode(e.code);
		return response;
	return Response(connection);	
	
	
##  Github Commit Test

# testb = staticmethod(testb);



