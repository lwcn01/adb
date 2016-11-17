#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,os
from Utils.adb import *
from Utils.util import *
"""
设备信息
"""

def DeviceInfo():
    adb = Adb()
    if adb_env:
        status = adb.adb("get-serialno").stdout.read().decode('utf-8').strip()
        if status == 'unknown':
            print("\nADB-Connect...Fail")
        else:
            print("\nADB-Connect...OK\n")
            model = adb.DeviceModel()
            sys_version = adb.AndroidVersion()
            brand = adb.shell("getprop ro.product.brand").stdout.read().decode('utf-8').strip()
            display_resolution = adb.shell("wm size").stdout.read().decode('utf-8').strip()
            if os.name == 'nt':
                find = 'findstr'
            else:
                find = 'grep'
            get_ip = adb.shell("ip addr | %s global" %find).stdout.read().decode('utf-8').strip()
            if "/" in get_ip.split()[1]:
                ip = get_ip.split()[1].split("/")[0]
            else:
                ip = get_ip.split()[1]
            get_mac = adb.shell("cat /sys/class/net/eth0/address").stdout.read().decode('utf-8').strip()
            if "/sys/class/net/eth0/address" in get_mac:
                wifi = adb.shell("dumpsys wifi").stdout.readlines()[0].decode('utf-8').strip()
                if "enabled" in wifi:
                    net = "无线网卡"
                    mac = adb.shell("cat /sys/class/net/wlan0/address").stdout.read().decode('utf-8').strip()
            else:
                net = "有线网卡"
                mac = get_mac
            print("产品品牌：" + brand,
                  "产品型号：" + model,
                  "产品IP地址：" + ip,
                  "%sMAC地址：" %net + mac,
                  "系统版本：" + sys_version,
                  "系统分辨率：" + display_resolution.split(":")[1],
                  sep = '\n')
    Pause()

if __name__ == '__main__':
    DeviceInfo()
