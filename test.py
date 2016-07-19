#coding=utf8
from OpenstackApiServer import OpenstackApiServer

"""url = 'http://api.douban.com/v2/book/isbn/9787218087351'
postData = {'number': 12524, 'type': 'issue', 'action': 'show'}
httpUrlRequest = HttpUrlRequest()
res = httpUrlRequest.httpPost(url, postData)
a = httpUrlRequest.stringToDict(res)
for val in a:
    if val == 'rating':
        print 'key值为rating的value:',a[val]"""


openstackApiServer = OpenstackApiServer()
openstackApiServer.run()
