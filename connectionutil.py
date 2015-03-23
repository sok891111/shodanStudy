# connectionutil
# @author : SJ
# @date : 2015.03.22
# @purpose : connectionutil for shodan study
#			 try loging WAS manager page

import json, urllib2, httputil;

# read json file
def getPasswordList():
	pwFile="./config/passwd.json";
	f = open(pwFile, 'r');
	js = json.loads(f.read());
	f.close();
	return js;


# read config file and try login based on userInfo from config file
# return response obj(httputil)	
def server_opener(response):
	serverName = response.getServerInfo();

	## TO_DO : adding url based on different WAS
	if serverName.lower() == "tomcat" :
		suffix = "manager/";
	else :
		suffix = "manager/";

	## making WAS manager url
	if response.getUrl()[-1] == "/" :
		url = response.getUrl() + suffix;
	else : 
		url = response.getUrl() + "/" +suffix;

	## copy python authentication sample
	pwList = getPasswordList().get(serverName);
	passman = urllib2.HTTPPasswordMgrWithDefaultRealm();

	## add passwd list from config file
	for key in pwList.keys():
		passman.add_password(None, url , key, pwList.get(key));
	authhandler = urllib2.HTTPBasicAuthHandler(passman);
	opener = urllib2.build_opener(authhandler);
	urllib2.install_opener(opener);
	req = httputil.Request(url);

	# convert httputil response obj and return it
	return httputil.httpRequest(req);
