#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Utils.adb import *
from Utils.util import *
"""
一键卸载Android系统所有第三方APK
"""
def Uninstall():
    applist = ThirdAppList()
    count = len(applist)
    print("共：%s 个应用\n" %count)
    AppUninstall(*applist)
    print('卸载完成！')

if __name__ == '__main__':
    adb = Adb()
    status = adb.DeviceStatus()
    if 'device' == status:
        print("0 卸载单个应用\n1 卸载全部应用\n")
        num = int(input("输入数字："))
        if num == 0:
            AppUninstall(CurrentPackageName()[0])
            print('\n卸载完成！')
        elif num == 1:
            Uninstall()
        else:
            pass
    else:
        print('adb disconnect')
    Pause()
