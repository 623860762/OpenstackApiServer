#coding=utf8
import httplib, urllib, urllib2, json

class HttpUrlRequest:
    timeout = ""
    def __int__(self, timeout):
        self.timeout = timeout
    #post请求
    #参数：url:string, post_data:json格式dict
    #返回：json格式string
    def httpUrlPost(self, url, postData):
        data = urllib.urlencode(postData)
        headers = {"Content-type": "application/json","Accept": "text/plain"}
        try:
            #获取request请求句柄
            request = urllib2.Request(url, headers)
            #添加json参数，header等
            request.add_data(data)
            print request.get_method(), '请求参数:', request.get_data()
            res = urllib2.urlopen(request)
            resData = res.read()
            print '返回数据：',resData
            #关闭请求
            res.close()
        except:
            return -1
        return resData
    #get请求
    #参数：url:string
    #返回：json格式string
    def httpUrlGet(self, url):
        try:
            request = urllib2.Request(url)
            print request.get_method(), '请求参数:', request.get_data()
            res = urllib2.urlopen(request)
            resData = res.read()
            print '返回数据：',resData
            res.close()
        except:
            return -1
        return resData
    #函数：将dict对象转换成string类型
    def dictToString(self,dict):
        return json.dumps(dict)
    #函数：将string类型转换成dict类型
    def stringToDict(self,string):
        return json.loads(string)
    #http请求,若params=="",get请求，若params!="",post请求
    def httpRequest(self, url, params,headers):
        hostPortRestString = self.getHostPortRestFromUrl(url)
        host = hostPortRestString['host']
        port = hostPortRestString['port']
        rest = hostPortRestString['rest']
        # 3 params: host,port,timeout
        conn = httplib.HTTPConnection(host,port,self.timeout)
        #函数：url编码
        #params = urllib.urlencode(params)
        #post，get请求判断
        if params=="":
            conn.request("GET", rest, params, headers)
        else:
            #将json对象转换成str对象
            params = json.dumps(params)
            # 4 params: method,url,data,headers
            conn.request("POST", rest, params, headers)
        res = conn.getresponse()
        #print res.getheader('x-subject-token')
        print "post请求：",params, res.status, res.reason
        resData = res.read()
        print  "返回数据：", resData
        res.close()
        return resData
    #getResponseHeaders获取resoponse头
    def getSubjectToken(self, url, params,headers):
        hostPortRestString = self.getHostPortRestFromUrl(url)
        host = hostPortRestString['host']
        port = hostPortRestString['port']
        rest = hostPortRestString['rest']
        # 3 params: host,port,timeout
        conn = httplib.HTTPConnection(host,port,self.timeout)
        #函数：url编码
        #params = urllib.urlencode(params)
        #post，get请求判断
        if params=="":
            conn.request("GET", rest, params, headers)
        else:
            #将json对象转换成str对象
            params = json.dumps(params)
            # 4 params: method,url,data,headers
            conn.request("POST", rest, params, headers)
        res = conn.getresponse()
        #获取list头部信息
        #resHeaders = res.getheaders()
        subToken = res.getheader('x-subject-token')
        #print
        print "post请求：",params, res.status, res.reason
        resData = res.read()
        print  "返回数据：", resData
        res.close()
        return subToken

    #url中获取主机，端口和rest信息json格式
    def getHostPortRestFromUrl(self,url):
        proto, rest = urllib.splittype(url)
        host, rest = urllib.splithost(rest)
        host, port = urllib.splitport(host)
        if port is None:
            port = 80
        hostPortRest = {}
        hostPortRest['host'] = host
        hostPortRest['port'] = port
        hostPortRest['rest'] = rest
        return hostPortRest


