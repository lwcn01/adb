#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.adb import *
from Utils.util import *
"""
抓取APP数据包，文件保存在桌面log目录下
"""
adb = Adb()
def tcp_dump(num):
    timestamp = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    capture_path = "/sdcard/" + timestamp + ".pcap"
    path = CreateDir('path3')
    TcpDump(capture_path,num).wait()
    Pull(capture_path,path).wait()
    adb.shell("rm -r " + capture_path)

if __name__ == '__main__':
    status = adb.DeviceStatus()
    if 'device' == status:
        num = int(input("抓取数据包的个数："))
        tcp_dump(num)
        print("抓包文件位置 ---> " + CreateDir('path3'))
    else:
        print('adb disconnect')
    Pause()
