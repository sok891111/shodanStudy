# connectionutil
# @author : SJ
# @date : 2015.03.22
# @purpose : connectionutil for shodan study
#			 try loging WAS manager page

import json;

# read json file
def getPasswordList():
	pwFile="./config/passwd.json";
	f = open(pwFile, 'r');
	js = json.loads(f.read());
	f.close();
	return js;


