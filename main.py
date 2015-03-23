from httputil import *;
from connectionutil import *;

url ="http://118.176.52.12:8080"
request = Request(url);
response = httpRequest(request);

if response.isSuccess() : 
	result = server_opener(response);
	if result.isSuccess() :
		print "login Success";
	else :
		message = "[Status Code "+str(result.getStatusCode()) +"] >>> login Fail";
		print message;