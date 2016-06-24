#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.adb import *
from Utils.util import *
"""
Android 4.4+以上系统支持屏幕录制功能
"""
adb = Adb()
def screen_record():
    timestamp = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    video_path = "/data/local/tmp/" + timestamp + ".mp4"
    screen_dir = CreateDir('path2')
    ScreenRecord(video_path).wait
    num = input("回车键停止录制")
    if num =='':
        adb.adb('kill-server')
    Pull(video_path,screen_dir).wait()
    adb.shell("rm -r " + video_path)

if __name__ == "__main__":
    sdk_version = adb.SdkVersion()
    status = adb.DeviceStatus()
    if 'device' == status:
        if int(sdk_version) > 19:
            screen_record()
            print('录制成功 ---> ' + CreateDir('path2'))
        else:
            print('Android版本低于4.4，无法录制')
    else:
        print('adb disconnect')
    Pause()
