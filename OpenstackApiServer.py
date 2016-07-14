#coding=utf8
from HttpUrlRequest import HttpUrlRequest
import json
class OpenstackApiServer:

    #def __int__(self):
        #self.token = token
    #获取认证token,1小时有效
    #参数：url:string, postData:dict
    #返回: id:string
    def getTokenId(self, url, postData):
        httpUrlRequest = HttpUrlRequest()
        headers = {"Content-type": "application/json","Accept": "text/plain"}
        subToken = httpUrlRequest.getSubjectToken(url,postData,headers)
        return subToken
    #测试认证方法
    def test(self,tokenId, url, postData):
        ob1 = HttpUrlRequest()
        headers = {"Content-type": "application/json","Accept": "text/plain","X-Auth-Token": tokenId}
        res = ob1.httpRequest(url,postData,headers)
        print res
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

url = 'http://172.17.1.10:5000/v3/auth/tokens'
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
openstackApiServer = OpenstackApiServer()
tokenId = openstackApiServer.getTokenId(url,postData)
url = 'http://172.17.1.10:5000/v3/roles'
postData = {
    "group": {
        "description": "Contract developers",
        "domain_id": "default",
        "name": "Contract developers"
    }
}
openstackApiServer.test(tokenId,url,postData)
