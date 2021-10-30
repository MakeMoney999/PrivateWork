import os
import socket

def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip



def main():
	ip=get_host_ip()
	port="8080"
	cmd = "mitmdump -q -s wechat_login.py"
	print ("代理服务器已启动")
	print ("请配置wifi代理模式,ip:"+ip,"端口号:"+port)
	print ("配置完成后请打开浏览器访问www.jcgame.net进行链接测试")
	output=os.system(cmd)

if __name__ == '__main__':
	main()