#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.adb import *
from Utils.util import *
"""
Android 4.4+以上系统支持屏幕录制功能
"""
adb = Adb()
def screen_record(times):
    global screen_dir
    timestamp = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    video_path = "/data/local/tmp/" + timestamp + ".mp4"
    path = "--time-limit %s " %times + video_path
    screen_dir = CreateDir('path3')
    ScreenRecord(path).wait()
    Pull(video_path,screen_dir).wait()
    adb.shell("rm -r " + video_path)

if __name__ == "__main__":
    sdk_version = adb.SdkVersion()
    status = adb.DeviceStatus()
    if 'device' == status:
        if int(sdk_version) > 19:
            times = input('屏幕录制时长：')
            print('开始屏幕录制')
            if times == '':
                screen_record(180)
                print('录制成功 ---> ' + screen_dir)
            else:
                try:
                    times = int(times)
                except Exception as e:
                    print(e)
                else:
                    screen_record(int(times))
                    print('录制成功 ---> ' + screen_dir)
        else:
            print('Android版本低于4.4，无法录制')
    else:
        print('adb disconnect')
    Pause()
