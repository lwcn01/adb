#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'new'

import os,re
import time
from Utils.util import Adb
Adb = Adb()
def Connect(ip):
    """
    :Args:
    -ip- <host>[:<port>]
    :Usage:
        Connect(ip)
    """
    return Adb.adb("connect %s" %ip)

def DisConnect(ip):
    return Adb.adb("disconnect %s" %ip)

def DeviceList():
    return Adb.adb("devices -l").stdout.read().strip()

def Push(local_path,remote_path):
    """
    :Args:
    -local_path- path on PC
    -remote_path- path on mobile device
    :Usage:
        Push(local_path,remote_path)
    """
    return Adb.adb("push %s %s" %(local_path,remote_path))

def Pull(remote_path,local_path):
    return Adb.adb("pull %s %s" %(remote_path,local_path))

def Sync():
    """
    copy host->device only if changed
    """
    return Adb.adb("sync")

def Bugreport():
    try:
        #utf-8编码文件，忽略非法编码字符
        f = open(os.path.join(os.getcwd(),'bugreport.log'),'w',encoding='utf-8',errors='ignore')
    except IOError:
        pass
    else:
        f.write(Adb.adb("bugreport").stdout.read())
    finally:
        f.close()
    return

def AdbVersion():
    return Adb.adb("version")

def Reboot():
    return Adb.adb("reboot")

def FastBoot(self):
    return Adb.adb("reboot bootloader")

def AppList():
    AppList = []
    for package in Adb.shell("pm list package").stdout.readlines():
        AppList.append(re.split(r'[:=]',str(package))[-1].splitlines()[0])
    for i in range(len(AppList)):
        AppList[i] = AppList[i].split("\\")[0]
    return AppList

def SystemAppList():
    SystemAppList = []
    for package in Adb.shell("pm list package -s").stdout.readlines():
        SystemAppList.append(re.split(r'[:=]',str(package))[-1].splitlines()[0])
    for i in range(len(SystemAppList)):
        SystemAppList[i] = SystemAppList[i].split("\\")[0]
    return SystemAppList

def ThirdAppList():
    ThirdAppList = []
    for package in Adb.shell("pm list package -3").stdout.readlines():
        ThirdAppList.append(re.split(r'[:=]',str(package))[-1].splitlines()[0])
    for i in range(len(ThirdAppList)):
        ThirdAppList[i] = ThirdAppList[i].split("\\")[0]
    return ThirdAppList

def AppPath(*PackageName):
    AppPathlist = []
    for i in PackageName:
        for package_path in Adb.shell("pm list package -f %s" %i).stdout.readlines():
            AppPathlist.append(str(package_path).split(":")[-1].split("=")[0])
    return AppPathlist

def IsAppInstall(PackageName):
    if PackageName in AppList():
        return True
    else:
        return False

def AppInstall(App_path):
    """
    APK在PC端
    """
    return Adb.adb('install -r %s' %App_path)

def PmInstall(App_path):
    """
    APK在mobile端
    """
    return Adb.shell('pm install -r %s' %App_path)

def AppUninstall(*PackageName):
    for i in PackageName:
        if IsAppInstall(i):
            Adb.adb('uninstall %s' %i)
    return

def ClearAppData(PackageName):
    if IsAppInstall(PackageName):
        return Adb.shell('pm clear %s' %PackageName)

def AppPid(PackageName):
    PidInfo = Adb.shell("ps | grep %s" %PackageName).stdout.read()
    if PidInfo !='':
        return re.split(r'\s+',PidInfo)[1]

def KillProcess(PackageName):
    if AppPid(PackageName):
        Pid = AppPid(PackageName)
        return Adb.shell("kill -9 %d" %int(Pid))

def QuitApp(PackageName):
    if AppPid(PackageName):
        return Adb.shell("am force-stop %s" %PackageName)

def AppInfo(PackageName):
    if IsAppInstall(PackageName):
        with open(os.path.join(os.getcwd(),'AppInfo.txt'),'w') as f:
            f.write(Adb.shell('pm dump %s' %PackageName).stdout.read())
    return

def ScreenShot(pic_path):
    return Adb.shell("screencap -p " + pic_path)

def ScreenRecord(video_path):
    return Adb.shell("screenrecord " + video_path)

def TcpDump(capture_path,num):
    return Adb.shell("tcpdump -s 10000 -c %s -w " %num + capture_path)

def CurrentPackageName():
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    Adb.adb("wait-for-device")
    if os.name == 'nt':
        find = 'findstr'
    else:
        find = 'grep'
    out = Adb.shell("dumpsys window w | %s \/ | %s name=" %(find, find)).stdout.read()
    PackageName = pattern.findall(str(out))[0].split("/")[0]
    Activity = pattern.findall(str(out))[0].split("/")[1]
    return PackageName,Activity         # 以元组返回

def Pause():
    return Adb.shell(os.system('pause'))

def CreateDir(num):
    desktop = os.path.expanduser('~') + '\Desktop'
    path1 = os.path.join(desktop,'app')
    package = AppPath(CurrentPackageName()[0])[0].split("/")[-1]
    app_name = re.findall(r"(.*)\.apk",package)
    path2 = os.path.join(desktop,app_name[0])
    path3 = os.path.join(desktop,'log')
    if num == 'path1':
        if not os.path.exists(path1):
            os.mkdir(path1)
        return path1
    elif num == 'path2':
        if not os.path.exists(path2):
            os.mkdir(path2)
        return path2
    elif num == 'path3':
        if not os.path.exists(path3):
            os.mkdir(path3)
        return path3

def Web(url):
    """
    :Args:
    -url- domain name
    :Usage:
        Web('[domain name]')
    """
    url = "http://" + url
    return Adb.shell("am start -a android.intent.action.VIEW -d %s" %str(url))

def Phone(num):
    return Adb.shell("am start -a android.intent.action.CALL -d tel:%s" %str(num))
