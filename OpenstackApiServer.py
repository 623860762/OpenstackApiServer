#coding=utf8
from HttpUrlRequest import HttpUrlRequest

class OpenstackApiServer:


    #def __int__(self):
        #self.token = token
    #获取认证token
    #参数：url:string, username:string, password:string, tenantId:string
    #返回: id:string
    def getToken(self, url, postData):
        httpUrlRequest = HttpUrlRequest()
        httpUrlRequest.httpUrlPost(url,postData)
        return 'Token'
    #启动实例
    #参数：
    #返回:
    def startServer(self,id):
        try:
            httpUrlRequest = HttpUrlRequest()
        except:
            return -1
        return id
    #关闭实例
    #参数：
    #返回:
    def stopServer(self,id):
        try:
            httpUrlRequest = HttpUrlRequest()
        except:
            return -1
        return id
    #查看实例状态
    #参数：id
    #返回:
    def showServer(self,id):
        try:
            httpUrlRequest = HttpUrlRequest()
        except:
            return -1
        return id

#url = 'http://api.douban.com/v2/book/isbn/9787218087351'
#postData ={"auth":{"passwordCredentials":{"username":"admin","password":"123456"}}}

