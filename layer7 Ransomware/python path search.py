import os
from pathlib import Path
from getpass import getuser
import time

userPath='/Users/name/Desktop/hello'.replace('name',getuser())
p = Path(userPath)


start = time.time()  # 시작 시간 저장

"""
for (path, dir, files) in os.walk(userPath):
    try:
        for filename in files:
            full_filename=(path+'/'+filename)
            #a.encrypt_file(full_filename)
            print(full_filename)
    except (PermissionError, ValueError):
        pass

"""


for x in tuple(p.glob("**/*")):
    try:
        print(str(x))
    except (PermissionError, ValueError):
        pass
    #print(str(x)+"=success encryption")

 
 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
