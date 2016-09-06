#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import operator
from functools import reduce
from PIL import Image
from Utils.adb import *
from Utils.util import *
"""
图片对比
"""

def screenShot():
    timestamp = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    pic_path = "/data/local/tmp/" + timestamp + ".png"
    ScreenShot(pic_path).wait
    time.sleep(3)
    screen_dir = CreateDir('path2')
    Pull(pic_path,screen_dir).wait()
    adb.shell("rm -r " + pic_path)
    return screen_dir + "\\" + timestamp + ".png"

def filePath(path): 
    if os.path.exists(path):
        if os.path.isfile(path):
            return path.strip()

def imageSimilarity(f1, f2):
    #完全相似结果为0
    image1 = Image.open(f1)
    image2 = Image.open(f2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    diff = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )

    return diff

if __name__ == "__main__":
    adb = Adb()
    status = adb.DeviceStatus()
    if 'device' == status:
        print("\n截图中...")
        f1 = screenShot()
        print("\n截图完成...")
        path = input("\n本地图片路径：")
        f2 = filePath(path)
        p = imageSimilarity(f1, f2)
        print("\n图片差距...",p)
        print("\n图片对比完成...")
    else:
        print('adb disconnect')
    Pause()