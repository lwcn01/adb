#!/usr/bin/env python
"""
说明：
1. python3.x环境 + Android开发环境
2. Utils包封装了一些adb命令,脚本文件依赖于该包
3. /adb/目录下*.py文件是可执行文件，具体实现功能查看对应代码注释
4. *.py文件基本未做异常处理,需要先让adb连接上设备，才能使用
"""
from setuptools import setup

setup(
  name='adb',
  version='1.0',
  description='rely on py3',
  author='new',
  author_email=' ',
  url='http://127.0.0.1:8080',
  packages=['Utils'],
)
