#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,os
from Utils.adb import *
from Utils.util import *
"""
检测adb连接状态
"""

def status():
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
            print("\nadb连接...OK")
        else:
            print("\nadb连接...失败")
    Pause()

def main():
    adb = Adb()
    status()
    adb.adb("kill-server").wait()
    print("\nadb连接中...")
    adb.adb("start-server").wait()
    time.sleep(3)
    ip = input("\n请输入移动端IP地址：")
    try:
        info = Connect(ip.strip())
    except Exception as e:
        print(e)
    else:
        print(info.stdout.read().strip().decode('utf-8'))
    finally:
        status()
    
if __name__ == '__main__':
    main()