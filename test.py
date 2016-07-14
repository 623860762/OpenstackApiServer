#coding=utf8
import httplib, urllib, urllib2, json
from HttpUrlRequest import HttpUrlRequest

"""url = 'http://api.douban.com/v2/book/isbn/9787218087351'
postData = {'number': 12524, 'type': 'issue', 'action': 'show'}
httpUrlRequest = HttpUrlRequest()
res = httpUrlRequest.httpPost(url, postData)
a = httpUrlRequest.stringToDict(res)
for val in a:
    if val == 'rating':
        print 'key值为rating的value:',a[val]"""


#httpPost请求：
url = 'http://172.17.1.10:5000/v3/auth/tokens'
#url = 'http://api.douban.com/v2/book/isbn/9787218087351'
#url = "http://192.168.4.102:5000/v3"
postData = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "admin",
                    "domain": {
                        "name": "default"
                    },
                    "password": "123456"
                }
            }
        }
    }
}
headers = {"Content-type": "application/json","Accept": "text/plain"}
httpUrlRequest = HttpUrlRequest()
resHeaders = httpUrlRequest.getResponseHeaders(url,postData,headers)