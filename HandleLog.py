#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
"""
过滤Log日志
+100 最前一百行 
-100 最后一百行
"""
def rFile(path):
    path = path.strip()
    if "\"" in path:
        path = path.strip("\"")
    elif "\'" in path:
        path = path.strip("\'")
    timestamp = time.strftime('%Y-%m-%d_%H.%M.%S',time.localtime(time.time()))
    if not os.path.exists(path):
        print("\nFile Not Found...")
    elif not os.path.isfile(path):
        print("\nNone File...")
    elif os.path.splitext(path)[-1] != ".log" and os.path.splitext(path)[-1] != ".txt":
        print("\nNone Log File...")
    else:
        text = os.path.join(os.path.dirname(path),"Log_" + timestamp + ".log")   
        writeLog = open(text,'w',encoding='utf-8',errors='ignore')
        rank = input("\nLog Rank（Enter means view lines）：")
        if rank.islower():
            rank = rank.upper()
        with open(path,'r',encoding='utf-8',errors='ignore') as f:
            data = f.readlines()
            if rank == "V" or rank == "D" or rank == "I" or rank == "W" or rank == "E":
                for txt in data:
                    try:
                        txt.split("/")[0]
                    except Exception as e:
                        print("\n%s Filter Error：%s"%(rank,e))
                    else:
                        if rank in txt.split("/")[0]:
                            writeLog.write(txt)
                        else:
                            try:
                                txt.split()[2].split("/")[0]
                            except Exception:
                                pass
                            else:
                                if rank in txt.split()[2].split("/")[0]:
                                    writeLog.write(txt)
            elif rank == "":
                choose = input("\nView Forward or Afterward：")
                line = input("\nInput Lines：")
                if int(line) > int(len(data)):
                    print("\nOver The Max lines...")
                else:
                    if choose == "+":
                        lines = int(line)
                    elif choose == "-":
                        lines = -int(line)
                    if lines > 0:
                        for i in range(lines):
                            writeLog.write(data[i])
                    elif lines < 0:
                        for i in range(lines,0):
                            writeLog.write(data[len(data) + i])
            else:
                pass      
            writeLog.close()
        if not os.path.getsize(text):
            os.remove(text)
            print("\nLog Not Found...")
        print("\nHandleLog Completed...")             

if __name__ == '__main__':
    path = input("\nLog Path：")
    rFile(path)
    os.system("pause")
