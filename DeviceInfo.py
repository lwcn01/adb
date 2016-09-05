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
            print("产品品牌：" + brand,"产品型号：" + model,"系统版本：" + sys_version,sep = '\n')
    Pause()

if __name__ == '__main__':
    DeviceInfo()