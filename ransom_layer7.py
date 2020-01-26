from Crypto.Cipher import AES 
from Crypto import Random
import base64 #base64로 encoding 하기 위해 
import hashlib


"""
문자열을 encrypt에 인자로 전달시 입력 받은 데이터의 길이가 BLOCK_SIZE의
배수가 아닐 때 padding이 필요하다. AES에서는 BLOCK_SIZE가 128bit
즉 16bit로 고정되는데, 아래 코드를 통해 자동 패딩 처리한다. 한글에 대한 처리를
위해 pad 시에 len(s.encode('utf-8')) 처리가 반드시 필요하다. 영문과
기호는 문자당 1byte지만 한글은 문자당 2바이트이기 때문이다. len() 함수를 활용해
길이를 통해 바이트 계산을 하는 방식이므로 'utf-8' 변환하지 않을 경우 오류
가 발생하게 된다.
"""
BS=AES.block_size #16
#padding을 위한 함수
pad=lambda s: s+(BS-len(s.encode('utf-8'))%BS)* chr(BS - len(s.encode('utf-8')) % BS)
#unpadding을 위한 함수
unpad = lambda s : s[:-ord(s[len(s)-1:])]

data = "Iran has seized a foreign oil tanker in the Persian Gulf that was smuggling fuel to some Arab states, according to a state television report on Sunday. The report said that the tanker had been detained and the ship's foreign crew held by the country's elite Islamic Revolutionary Guards Corps."
key = "this is a key123".encode('utf-8')

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


encrypted_data = AESCipher(bytes(key)).encrypt(data)  
print(encrypted_data)

decrypted_data = AESCipher(bytes(key)).decrypt(encrypted_data)
print(decrypted_data.decode('utf-8'))
