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
    AppUninstall(*applist)
    print('卸载完成！')

if __name__ == '__main__':
    adb = Adb()
    status = adb.DeviceStatus()
    if 'device' == status:
        Uninstall()
    else:
        print('adb disconnect')
    Pause()