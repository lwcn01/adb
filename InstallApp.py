#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
from Utils.adb import *
from Utils.util import *
"""
0 apps目录在电脑桌面
1 apps目录在Sdcard目录下
2 apps目录在外设下
3 安装单个apk文件
"""
def adb_insatll():
    desk = os.path.expanduser('~') + '\Desktop'
    path = desk + "\\apps"
    if os.path.exists(path):
        count = 0
        print("\n应用安装中...")
        for f in os.listdir(path):
            if os.path.splitext(f)[-1] == ".apk":
                app_path = path + "\\" + f
                try:
                    AppInstall(app_path).wait()
                except Exception as e:
                    print(e)
                else:
                    count += 1
                    print(os.path.splitext(f)[0] + " ——> Success")
        print("\n共安装应用 %s 个" %count)            

def pm_install(remote_path):
    try:
        adb.shell("ls %s" %remote_path)
    except Exception as e:
        print(e)
    else:
        count = 0
        print("\n应用安装中...")
        for i in adb.shell("ls %s" %remote_path).stdout.readlines():
            f = i.strip().decode("utf-8")
            if f.split(".")[-1] == "apk":
                app_path = "%s" %remote_path + "\/" + f
                try:
                    PmInstall(app_path).wait()
                except Exception as e:
                    print(e)
                else:
                    count += 1
                    print(f.split(".")[0] + " ——> Success")
        print("\n共安装应用 %s 个" %count)

def single_app():
    path = input("\n本地文件路径：")
    if not os.path.exists(path.strip()):
        print("\n路径不存在")
    elif not os.path.isfile(path.strip()):
        print("\n文件错误")
    elif os.path.splitext(path.strip())[-1] == ".apk":
        try:
            print("\n应用安装中...")
            AppInstall(path.strip()).wait()
        except Exception as e:
            print(e)
        else:
            print("\nSuccess")
    else:
        print("\n非APK文件")

def ExtendStorage():
    sdk = adb.SdkVersion()
    for info in adb.shell("cat /proc/partitions").stdout.readlines():
        if len(info.strip()) != 0:
            i = info.strip().decode("utf-8")
            if "sd" in i:
                if int(sdk) >= 17:
                    for usb in adb.shell("ls /storage/external_storage").stdout.readlines():
                        usb = usb.strip().decode("utf-8")
                        if "udisk" in usb:
                            usb_name = usb
                            remote_path = "/storage/external_storage/%s/apps" %usb_name
                            break
                        elif "sda" in usb:
                            usb_name = usb
                            remote_path = "/storage/external_storage/%s/apps" %usb_name
                            break
                        elif "sdb" in usb:
                            usb_name = usb
                            remote_path = "/storage/external_storage/%s/apps" %usb_name
                            break
                    return remote_path
    
                elif int(sdk) < 17:
                    for usb in adb.shell("ls /mnt").stdout.readlines():
                        usb = usb.strip().decode("utf-8")
                        if "sda" in usb:
                            usb_name = usb
                            remote_path = "/storage/external_storage/%s/apps" %usb_name
                            break
                        elif "sdb" in usb:
                            usb_name =usb
                            remote_path = "/storage/external_storage/%s/apps" %usb_name
                            break
                     
                    return remote_path                            

            elif "card" in i:
                for card in adb.shell("ls /storage/external_storage").stdout.readlines():
                    card = card.strip().decode("utf-8")
                    if "sdcard" in card:
                        card_name = card
                        remote_path = "/storage/external_storage/%s/apps" %card_name
                
                        return remote_path
    
if __name__ == '__main__':
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
            print("\n0 apps目录在电脑桌面\n1 apps目录在Sdcard目录下\n2 apps目录在外设下\n3 安装单个apk文件\n")
            number = int(input("输入数字："))
            if number == 0:
                adb_insatll()
            elif number == 1:
                pm_install("/sdcard/apps")
            elif number == 2:
                remote_path = ExtendStorage()
                pm_install(remote_path)
            elif number == 3:
                single_app()
            else:
                pass
        else:
            print("\nadb连接失败")
    else:
        print("\n环境变量错误")
    Pause()
