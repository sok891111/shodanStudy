from HttpUtil import *;
request = Request("http://www.naver.com");
response = httpRequest(request);
print response.getHeader();
