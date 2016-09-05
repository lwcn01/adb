#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Utils.adb import *
from Utils.util import *
"""
0. 获取移动端文件到本地PC桌面
1. 推送本地文件到移动端Sdcard目录
"""
def PushFile(pc_file):
    remote_path = "/sdcard/"
    local_path = pc_file.strip()
    Push(local_path,remote_path).wait()

def PullFile(mobile_file):
    """
    - usage: PullFile('xxx.txt')
    """
    local_path = os.path.expanduser('~') + '\Desktop'
    if len(mobile_file) == 0:
        print("\n路径错误")
        Pause()
        exit(1)
    elif "sdcard" not in mobile_file:
        if "\\" in mobile_file:
            mobile_file = mobile_file.strip("\\")
        remote_path = "/sdcard/" + mobile_file.strip("/")
    elif "\\" in mobile_file:
        remote_path = mobile_file.replace("\\","/")
    else:
        remote_path = mobile_file
    Pull(remote_path,local_path).wait()

if __name__ == '__main__':
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
            print("\n0 获取移动端文件到本地\n")
            print("1 推送本地文件到移动端\n")
            number = input('输入数字：')
            try:
                number = int(number)
            except Exception as e:
                print(e)
            else:
                if int(number) == 0:
                    mobile_file = input("\n移动端文件路径：")
                    try:
                        mobile_file = mobile_file.strip()
                        PullFile(mobile_file)
                    except Exception as e:
                        print(e)
                    else:
                        print("\n文件已保存至PC桌面")
                elif int(number) == 1:
                    # 直接将本地文件拖入该脚本窗口，即可获取路径
                    pc_file = input("\n本地文件路径：")
                    if pc_file.index("\"") != -1:
                        pc_file = pc_file[pc_file.index("\"")+1:]
                        if pc_file.rindex("\"") != -1:
                            pc_file = pc_file[:pc_file.index("\"")]
                    else:
                        pc_file = pc_file.strip()
                    if not os.path.exists(pc_file):
                        print("\n路径不存在")
                    elif not os.path.isfile(pc_file):
                        print("\n路径错误")
                    else:
                        try:
                            PushFile(pc_file)
                        except Exception as e:
                            print(e)
                        else:
                            print("\n文件已保存至移动端Sdcard目录")
        else:
            print("\nadb连接失败")
    else:
        print("\n环境变量错误")
    Pause()
