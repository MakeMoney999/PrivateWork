from mitmproxy.http import flow
import mitmproxy
import json
import os
import socket
import time
import subprocess







class wechat_app_login():

    def client_connected(self, client: mitmproxy.connection.Client):
        print ("客户端链接成功")
        a=1
        return a 

    def __init__(self,domain):
        self.domain=domain 
        self.url=domain+"/oauth/v2/wechat/mini-program/authorization-code/login"

    def request(self,flow):
        #print (self.url)
        if self.url in flow.request.url:
            requestbody=flow.request.get_content()
            requestbody=json.loads(requestbody)
            flow.request.set_text(json.dumps(requestbody))
            print(flow.request.get_text())

    def response(self,flow):
        if self.url in flow.request.url:
            print (flow.response.content)
            if flow.response.status_code == 200:
                res=flow.response.content  #login的返回
                start_Scrape(res[])#开始执行爬虫相关数据

        
addons = [
    wechat_app_login("https://oauth.marykayintouch.com.cn")
]