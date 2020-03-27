"""
암호화에 사용할 키는 어렵고 복잡하게 설정하는 것이 좋습니다.
하지만 키가 어렵다면 사람은 그것을 기억할 때 한계가 있으므로 hash를
쓰는 것도 좋은 방법입니다.
"""
from struct import pack,unpack,calcsize #파일 크기를 저장할 구조체 사용을 위해 
from Crypto.Cipher import AES
from Crypto import Random
from os import path,remove
#padding을 위한 함수
BS=16
pad=lambda s: s+(BS-len(s.encode('utf-8'))%BS)* chr(BS - len(s.encode('utf-8')) % BS)

class AEScipher:
    def __init__(self,key):
        self.key=pad(key).encode('utf-8')

    def encrypt_file(self,in_filename,out_filename=None):
        chunksize=64*1024 #65536
        if not out_filename:
            out_filename=in_filename+'.layer7'
        #initial vector
        iv=Random.new().read(16)
         # AES로 암호화된 키값을 생성
        encryptor=AES.new(self.key,AES.MODE_CBC,iv)
        filesize=path.getsize(in_filename)
        
        with open(in_filename,'rb') as infile:
            with open(out_filename,'wb') as outfile:
                outfile.write(iv)
                #Q=unsigned long long -> integer 8
                outfile.write(pack('Q',filesize))
                while True:
                    chunk=infile.read(chunksize)
                    if len(chunk)==0:
                        break
                    elif len(chunk) % 16!=0:
                        chunk+=b' '*(16-len(chunk)%16)
                    outfile.write(encryptor.encrypt(chunk))
        #기존에 있던 파일을 삭제시킨다.
        remove(in_filename)

    def decrypt_file(self,in_filename):
        chunksize=64*1024 
        out_filename=in_filename[:in_filename.rfind(".layer7")]
        with open(in_filename,'rb') as infile:
            iv=infile.read(16)
            #calcsize는 c코드로 변환된 구조체의 바이트 크기를 가져온다.
            original_size=unpack('Q',infile.read(calcsize('Q')))[0]
            decryptor = AES.new(self.key, AES.MODE_CBC, iv)
            
            with open(out_filename,'wb') as outfile:
                while True:
                    chunk=infile.read(chunksize)
                    if len(chunk) ==0:
                        break
                    #
                    outfile.write(decryptor.decrypt(chunk))
                    #원본 파일 크기로 자른다.
                    outfile.truncate(original_size)
        remove(in_filename)      


