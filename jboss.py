## @See : https://docs.python.org/2.7/library/urllib2.html?highlight=urllib#module-urllib2
## @See : http://j4ckp4rd.tistory.com/17 (Koean)
from urllib2 import *




url = "http://178.33.61.161:8080";
reqHeaer = {};
req = Request(url);
response = urlopen(req, None, 10);
# headers =  dict((x, y) for x, y in response.info().items());
print response.url;

# headers = response.info().keys();
# print url+">>"+"".join(headers);
# print headers;