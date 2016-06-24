#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
import subprocess
from Utils.adb import *
from Utils.util import *
"""
获取当前设备上已打开的应用的APK信息
"""

def app_info(tmp):
    if aapt_env():
        adb = Adb()
        remotePath = AppPath(CurrentPackageName()[0])
        Pull(remotePath[0],tmp).wait()
        subprocess.Popen("aapt dump badging %s" %(tmp+ "\\" + remotePath[0].split("/")[-1])).wait()

if __name__ == "__main__":
    tmp = tempfile.gettempdir()
    app_info(tmp)
    Pause()
