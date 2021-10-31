from mitmproxy.http import flow
import mitmproxy
import json
import os


class check_connect():
    """检查链接状态"""
    def request(self,flow):
        #print (flow.request.url)
        if "www.jcgame.net" in flow.request.url:
            print("连接成功")


class wechat_app_login():


    def __init__(self,domain):
        self.domain=domain 
        self.url=domain+"/oauth/v2/wechat/mini-program/authorization-code/login"

    def request(self,flow):
        #print (flow.request.url)
        if self.url in flow.request.url:
            requestbody=flow.request.get_content()
            requestbody=json.loads(requestbody)
            flow.request.set_text(json.dumps(requestbody))
            #print(flow.request.get_text())

    def response(self,flow):
        if self.url in flow.request.url:
            #print (flow.response.text)
            if flow.response.status_code == 200:
                res=json.loads(flow.response.text)  #login的返回
                access_token=res["access_token"]
                print (access_token)
                start_Scrape(access_token)#开始执行爬虫相关程序##############从这里写

        
addons = [
    check_connect(),
    wechat_app_login("https://oauth.marykayintouch.com.cn")
]