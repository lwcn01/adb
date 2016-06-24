#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Utils.adb import *
"""
清除当前已打开应用的数据及缓存
"""
if __name__ == '__main__':
    ClearAppData(CurrentPackageName()[0])
    print('success')
