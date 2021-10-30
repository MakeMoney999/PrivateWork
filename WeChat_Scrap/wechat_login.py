from mitmproxy.http import flow
import json


res={}

class wechat_app_login():

    def clientconnect(self, layer: mitmproxy.proxy.protocol.Layer):
        print ("设备连接成功")

    def __init__(self,domain):
        self.domain=domain 
        self.url=domain+"/oauth/v2/wechat/mini-program/authorization-code/login"

    def request(self,flow):
        print (self.url)
        if self.url in flow.request.url:
            requestbody=flow.request.get_content()
            requestbody=json.loads(requestbody)
            flow.request.set_text(json.dumps(requestbody))
            print(flow.request.get_text())

    def response(self,flow):
        global res
        if self.url in flow.request.url:
            print (flow.response.content)
            if flow.response.status_code == 200:
                res=flow.response.content
        
    # 状态码
    # print(flow.response.status_code)

    # 返回内容，已解码
    # print(flow.response.text)

    # 返回内容，Bytes类型
    # print(flow.response.content)

    # 取得响应的文本
    # print(flow.response.get_text())

    # 修改响应的文本
    # flow.response.set_text('123')

    # 返回404
    # flow.response = flow.response.make(404)

addons = [
    wechat_app_login("https://oauth.marykayintouch.com.cn")
]