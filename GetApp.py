#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Utils.adb import *
from Utils.util import *
"""
复制Android系统中应用的安装包到本地
"""
#PATH = lambda p: os.path.abspath(p)

def get_current_app():
    apkpath = AppPath(CurrentPackageName()[0])
    Pull(apkpath[0],appdir).wait()

def get_all_app():
    PackageName = AppList()
    apkpath = AppPath(*PackageName)
    for apk in apkpath:
        Pull(apk,appdir).wait()

def get_sys_app():
    PackageName = SystemAppList()
    syspath = AppPath(*PackageName)
    for apk in syspath:
        Pull(apk,appdir).wait()

def get_third_app():
    PackageName = ThirdAppList()
    thirdpath = AppPath(*PackageName)
    for apk in thirdpath:
        Pull(apk,appdir).wait()

if __name__ == '__main__':
    print("\n0 获取单个已打开应用的APK文件\n")
    print("1 获取Android系统中所有应用的APK文件\n")
    print("2 获取Android系统中系统应用的APK文件\n")
    print("3 获取Android系统中第三方应用的APK文件\n")
    digital = input('输入数字：')
    if adb_env():
        appdir = CreateDir('path1')
        if int(digital) == 0:
            get_current_app()
            print('single success->桌面app目录')
        elif int(digital) == 1:
            get_all_app()
            print('all success->桌面app目录')
        elif int(digital) == 2:
            get_sys_app()
            print('sys success->桌面app目录')
        elif int(digital) == 3:
            get_third_app()
            print('third success->桌面app目录')
        else :
            pass
    Pause()
