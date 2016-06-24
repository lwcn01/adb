#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from Utils.adb import *
from Utils.util import *
"""
截取当前屏幕，截图文件保存在桌面以当前打开的APP命名的文件夹下
"""
PATH = lambda p: os.path.abspath(p)
adb = Adb()
def screen_shot():
    timestamp = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    pic_path = "/data/local/tmp/" + timestamp + ".png"
    ScreenShot(pic_path).wait
    time.sleep(3)
    screen_dir = CreateDir('path2')
    Pull(pic_path,screen_dir).wait()
    adb.shell("rm -r " + pic_path)

if __name__ == "__main__":
    status = adb.DeviceStatus()
    if 'device' == status:
        screen_shot()
        print('截图成功 ---> ' + CreateDir('path2'))
    else:
        print('adb disconnect')
    Pause()
