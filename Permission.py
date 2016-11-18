#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
import json
from Utils.adb import *
from Utils.util import *

"""
获取设备上当前应用的权限列表
"""

PATH = lambda p: os.path.abspath(p)

def getPermission(packageName):
    permissionList = []
    if os.name == 'nt':
        find = 'findstr'
    else:
        find = 'grep'
    for permission in adb.shell("dumpsys package %s | %s android.permission" %(packageName, find)).stdout.readlines():
        permission = permission.decode("utf-8").strip()
        permissionList.append(permission)

    return permissionList

def handlePermission(packageName):
    permissionList = getPermission(packageName)
    permission_json_file = open(".\\permission.json",encoding = 'utf-8')
    file_content = json.load(permission_json_file)["PermissList"]
    if os.name == 'nt':
        f = open(PATH("%s/permission.txt" % CreateDir("path2")), "w")
        f.write("package: %s\n\n" %packageName)
        for permission in permissionList:
            for permission_dict in file_content:
                if permission == permission_dict["Key"]:
                    f.write("\n" + permission_dict["Key"] + ":\n  " + permission_dict["Memo"] + "\n")
        f.close
        print("permission.txt文件位置：" + CreateDir('path2') + "\n")
    else:
        print("package: %s\n" %packageName)
        for permission in permissionList:
            for permission_dict in file_content:
                if permission == permission_dict["Key"]:
                    print(permission_dict["Key"] + ":")
                    print("  " + permission_dict["Memo"])
    permission_json_file.close

if __name__ == '__main__':
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
             packageName = CurrentPackageName()[0]   
             handlePermission(packageName)
        else:
            print("\nadb连接失败")
    else:
        print("\n环境变量错误")
    Pause()     
