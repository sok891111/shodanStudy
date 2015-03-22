## @See : https://docs.python.org/2.7/library/urllib2.html?highlight=urllib#module-urllib2
## @See : http://j4ckp4rd.tistory.com/17 (Koean)
from urllib2 import *


url = "http://178.33.61.161:8080/web-console/";
accept ="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36";
origin = "www.naver.com"
reqHeaer = {"Accept" : accept,"User-Agent" : userAgent};
req = Request(url, None, reqHeaer, origin);
# print req.header_items();

headers = response.info().headers;
print url+">>"+"".join(headers);
print "";