import os
import socket
import time
import subprocess

command = "mitmdump -q -s wechat_login.py"
port="8080"

def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip

def run_mitmproxy(command):
	os.system(command)




def main():
	ip=get_host_ip()
	print ("代理服务器已启动")
	print ("请配置wifi代理模式,ip:"+ip,"端口号:"+port)
	print ("配置完成后请打开浏览器访问www.jcgame.net进行链接测试")
	run_mitmproxy(command)
	



if __name__ == '__main__':
	main()