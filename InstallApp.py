#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Utils.adb import *
from Utils.util import *
"""
0 apps目录在电脑桌面
1 apps目录在移动端Sdcard目录下
"""
def adb_insatll():
    desk = os.path.expanduser('~') + '\Desktop'
    path = desk + "\\apps"
    if os.path.exists(path):
        for f in os.listdir(path):
            if os.path.splitext(f)[-1] == ".apk":
                app_path = path + "\\" + f
                try:
                    AppInstall(app_path).wait()
                except Exception as e:
                    print(e)
                else:
                    print(os.path.splitext(f)[0] + " ——> Success")

def pm_install():
    try:
        adb.shell("ls /sdcard/apps")
    except Exception as e:
        print(e)
    else:
        for i in adb.shell("ls /sdcard/apps").stdout.readlines():
            f = i.strip().decode("utf-8")
            if f.split(".")[-1] == "apk":
                app_path = "/sdcard/apps/" + f
                try:
                    PmInstall(app_path).wait()
                except Exception as e:
                    print(e)
                else:
                    print(f.split(".")[0] + " ——> Success")

if __name__ == '__main__':
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
            print("0 apps目录在电脑桌面\n1 apps目录在移动端Sdcard目录下\n")
            number = int(input("输入数字："))
            if number == 0:
                adb_insatll()
            elif number == 1:
                pm_install()
            else:
                pass
        else:
            print("\nadb连接失败")
    else:
        print("\n环境变量错误")
    Pause()