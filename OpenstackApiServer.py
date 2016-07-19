#coding=utf8
from HttpUrlRequest import HttpUrlRequest
import json
class OpenstackApiServer:
    httpUrlRequest = HttpUrlRequest()
    #def __int__(self):
        #self.token = token
    #获取认证token,1小时有效
    #参数：url:string, postData:dict
    #返回: id:string
    def getTokenId(self, url, postData):
        headers = {"Content-type": "application/json","Accept": "text/plain"}
        subToken = self.httpUrlRequest.getSubjectToken(url,postData,headers)
        return subToken
    #测试认证方法
    def test(self,tokenId, url, postData):
        headers = {"Content-type": "application/json","Accept": "text/plain","X-Auth-Token": tokenId}
        print headers
        res = self.httpUrlRequest.httpRequest(url,postData,headers)
        print res
    #启动实例
    #参数：
    #返回:
    def startServer(self,id):
        try:
            a = "b"
        except:
            return -1
        return id
    #关闭实例
    #参数：
    #返回:
    def stopServer(self,id):
        try:
            a = "b"
        except:
            return -1
        return id
    #查看实例状态
    #参数：id
    #返回:
    def showServer(self,id):
        try:
            a = "b"
        except:
            return -1
        return id

    #启动4个虚拟机
    def run(self):
        url = 'http://172.17.1.10:5000/v3/auth/tokens'
        postData = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "domain": {
                                "id":"default",
                                "name": "default"
                            },
                            "name":"admin",
                            "password": "123456"
                        }
                    },
                },
                "scope": {
                    "project": {
                        "id":"132ba670ea1146528f23f31aa3e2b221"
                    }
                }
            }
        }
        openstackApiServer = OpenstackApiServer()
        #通过密码认证获取token_id
        tokenId = openstackApiServer.getTokenId(url,postData)
        #url = 'http://172.17.1.10:8774/v2/project_id/servers/93697d15-2843-4786-85f2-d0f41480fa6a/action'
        #url = 'http://172.17.1.10:8774/v2/132ba670ea1146528f23f31aa3e2b221/servers/93697d15-2843-4786-85f2-d0f41480fa6a/action'
        #url = "http://api.douban.com/v2/book/isbn/9787218087351"
        postData = {"os-stop" : "null"}
        openstackApiServer.test(tokenId,url,postData)
