#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from Utils.adb import *
from Utils.util import *
"""
打印Log
"""

def get_log():
    tfile = "Log_" + time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time())) + ".log"
    tpath = " >" + CreateDir('path3') + "\\" + tfile
    for i in range(5):
        adb.adb("logcat -c").wait()
    #adb.adb("logcat -v time -f /sdcard/test.log")
    adb.adb("logcat -v time" + tpath).wait()

if __name__ == '__main__':
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
            print("Log日志地址：" + CreateDir('path3') + "\n","\n======Log打印中=======")
            get_log()
        else:
            print("\nadb连接失败")
    else:
        print("\n环境变量错误")
    Pause()            