#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.adb import *
from Utils.util import *
"""
登录Web网页
"""

if __name__ == '__main__':
    adb = Adb()
    if adb_env:
        status = adb.DeviceStatus()
        if 'device' == status:
            # 在窗口输入域名地址即可，如：www.baidu.com
            url = input("\n输入url地址：")
            if type(url) == str:
                if url.strip().split(".")[0] == "www":
                    url = url.strip()
                else:
                    url = "www." + url.strip()
                try:
                    Web(url).wait()
                except Exception as e:
                    print(e)
            else:
                print("\n输入url不合法")
        else:
            print("\nadb连接失败")
    else:
        print("\n环境变量错误")
    Pause()
