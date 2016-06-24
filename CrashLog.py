#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Utils.adb import *
from Utils.util import *
"""
dropbox存储系统崩溃信息
未及时抓取APP的log时，通过dropbox获取其crash log
"""
adb = Adb()
def crash_time():
    if os.name == 'nt':
        find = 'findstr'
    else:
        find = 'grep'
    crash_time = adb.shell("dumpsys dropbox | %s data_app_crash" %find).stdout.readlines()
    timestamp = []
    for time in crash_time:
        l = []
        l.append(time.decode('utf-8').split()[0])
        l.append(time.decode('utf-8').split()[1])
        timestamp.append(" ".join(l))
    return timestamp

def crash_log(timestamp):
    times = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time())) + ".txt"
    with open(os.path.join(CreateDir('path3'),times),'w') as f:
        for t in timestamp:
            f.write(adb.shell("dumpsys dropbox --print %s" %t).stdout.read().decode('utf-8'))

if __name__ == '__main__':
    crash_log(crash_time())
    print('Crash日志存放 ---> ' + CreateDir('path3'))
    Pause()
