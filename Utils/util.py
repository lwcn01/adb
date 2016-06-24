#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ ='new'

import os
import re
import subprocess

def adb_env():
    if os.name == 'nt':
        env = os.getenv('PATH')
        adb_env = re.findall('platform-tools', env)
        if len(adb_env) == 0:
            raise EnvironmentError('env_configure error')
        elif len(adb_env) != 0:
            for i in re.split(';',env):
                adb_env = re.findall('[A-Za-z]\:.*\\platform-tools',i)
                if len(adb_env) != 0:
                    adb_env = adb_env[0]
                    break
            if 'adb.exe' not in os.listdir(adb_env):
                raise EnvironmentError('adb not found in platform-tools')
            else:
                return True
    else:
        return False

def aapt_env():
    if adb_env():
        aapte = os.environ['PATH']
        for i in aapte.split(';'):
            aaptv = re.findall('[A-Za-z]\:.*\\platform-tools',i)
            if len(aaptv) != 0:
                aaptv = aaptv[0]
                break
        if 'aapt.exe' not in os.listdir(aaptv):
            raise EnvironmentError('aapt not found in platform-tools')
        else:
            return True
    else:
        return False

class Adb(object):
    def __init__(self, DeviceId = ""):
        if DeviceId == "":
            self.DeviceId = ""
        else:
            self.DeviceId = "-s %s" %DeviceId

    def adb(self, args):
        """
        :Args:
        - args - adb command
        :Usage:
            Adb.adb('command')
        """
        cmd = "%s %s %s" % ('adb', self.DeviceId, str(args))
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def shell(self, args):
        """
        :Args:
        - args - shell command
        :Usage:
            Adb.shell('command')
        """
        cmd = "%s %s shell %s" % ('adb', self.DeviceId, str(args))
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def DeviceStatus(self):
        """设备状态
        device :  设备在线
        offline： 设备离线
        unknown： 设备未连接
        """
        return self.adb("get-state").stdout.read().decode('utf-8').strip()

    def DeviceID(self):
        """
        设备id号
        """
        return self.shell("getprop ro.serialno").stdout.read().decode('utf-8').strip()

    def AndroidVersion(self):
        """
        Android版本号
        """
        return self.shell("getprop ro.build.version.release").stdout.read().decode('utf-8').strip()

    def SdkVersion(self):
        """
        Android API
        """
        return self.shell("getprop ro.build.version.sdk").stdout.read().decode('utf-8').strip()

    def DeviceModel(self):
        """
        设备型号
        """
        return self.shell("getprop ro.product.model").stdout.read().decode('utf-8').strip()

    def MaxMermony(self):
        """
        内存阈值
        """
        return self.shell("getprop dalvik.vm.heapgrowthlimit").stdout.read().decode('utf-8').strip()
