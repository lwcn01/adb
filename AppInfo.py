#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tempfile
import subprocess
from Utils.adb import *
from Utils.util import *
"""
0 移动端的APK信息
1 电脑端的APK信息
"""

def get_package_info(spath):
    if aapt_env():
        try:
            package = subprocess.check_output("aapt dump badging %s" % spath)
        except Exception as e:
            print(e)
            Pause()
            exit(1)
        else:
            package_info = package.decode('utf-8')
            package_name = package_info.split('\n')[0].split("'")[1]
            versionCode = package_info.split('\n')[0].split("'")[3]
            versionName = package_info.split('\n')[0].split("'")[5]
            app_activity = re.findall(r'[a-zA-Z]{10}\-\w{8}\:\s+\w{4}\=(.*?)\s',package_info)
            app_name = re.findall(r"application-label-zh-CN\:\'(.*)\'",package_info)
            if len(app_name) == 0:
                app_name = re.findall(r"application-label-es\:\'(.*)\'",package_info)
                if len(app_name) == 0:
                    packagePath = AppPath(CurrentPackageName()[0])[0].split("/")[-1]
                    app_name = re.findall(r"(.*)\.apk",packagePath)
            print('应用名称：' + app_name[0],
                  '应用包名: ' + package_name,
                  '应用版本名: ' + versionName,
                  '应用版本号: ' + versionCode,
                  '应用Activity名：' + app_activity[0].strip("'"),
                  sep='\n')

def app_info(num):
    if int(num) == 0:
        tmp = tempfile.gettempdir()
        remotePath = AppPath(CurrentPackageName()[0])
        Pull(remotePath[0],tmp).wait()
        return tmp+ "\\" + remotePath[0].split("/")[-1]
    elif int(num) == 1:
        path = input('\n本地APK绝对路径：')
        if os.path.exists(path):
            if os.path.isfile(path):
                if os.path.splitext(path)[1] == ".apk":
                    return path
    else:
        pass

if __name__ == "__main__":
    print('\n========查看APK的基本信息========')
    print("\n0 移动端的APK信息")
    print("1 电脑端的APK信息\n")
    num = input('输入数字：')
    if int(num) == 0:
        adb = Adb()
        if adb_env:
            status = adb.DeviceStatus()
            if 'device' == status:
                spath = app_info(num)
                get_package_info(spath)
                inter = input("\n回车查看APK详情信息...")
                if inter == "":
                    subprocess.Popen("aapt dump badging %s" % spath).wait()
                else:
                    pass
            else:
                print("\nadb连接失败")
        else:
            print("\n环境变量错误")
    elif int(num) == 1:
        spath = app_info(num)
        if spath:
            get_package_info(spath)
            inter = input("\n回车查看APK详情信息...")
            if inter == "":
                subprocess.Popen("aapt dump badging %s" % spath).wait()
            else:
                pass
        else:
            print("\n本地APK路径错误")
    else:
        pass
    Pause()
