from httputil import *;

url ="http://www.naver.com"
request = Request(url);
response = httpRequest(request);

if response.isSuccess() : 
	result = server_opener(response);
	if result.isSuccess() :
		print "login Success";
	else :
		message = "[Status Code "+str(result.statusCode)+"] >>> login Fail" ;
		print message;
