#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import uuid
import socket
def get_mac_address():
    # 网卡MAC  
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def get_ip():
    #获取本机电脑名
    # name = socket.getfqdn() 可以不用传递参数
    name = socket.getfqdn(socket.gethostname())
    #获取本机ip
    addr = socket.gethostbyname(name)

    return name,addr

if __name__ == '__main__':
    print("电脑MAC：%s" % get_mac_address())
    print("电脑名：%s\n电脑IP：%s\n" % (get_ip()[0],get_ip()[1]))
    os.system("pause")