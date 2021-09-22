from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import sys, os
from django.conf import settings
import os

class Crypting:

    

    def __init__(self):
        file_add=os.path.join(settings.BASE_DIR,'steg/IV_file')
        print("iv file path:",file_add,type(file_add))
        with open(file_add,'rb') as iv_f:
            self.iv=iv_f.read(16)


    def encrypting(self,password,plaintext):
        
        #password=input("Enter password:").encode()
        key=hashlib.sha256(password).digest()

        cipher=AES.new(key, AES.MODE_CBC,self.iv)

        #plaintext=input("Enter your text:").encode()

        ciphertext=cipher.encrypt((pad(plaintext,AES.block_size)))

        #print(ciphertext)

        return ciphertext


    def decrypting(self, ciphertext,password):

        #password=input("Enter password:").encode()
        key=hashlib.sha256(password).digest()

        cipher = AES.new(key, AES.MODE_CBC, self.iv)

        try:
            plaintext=unpad(cipher.decrypt(ciphertext),AES.block_size)
            #print(plaintext.decode())
            return (0,plaintext.decode())
        except ValueError:
            #print("Wrong Password")
            return (-1,"Wrong Password")
        


if __name__=='__main__':
    ds=Crypting()
    a=ds.encrypting(input("Enter password:").encode(),input("Enter text:").encode())
    c,d=ds.decrypting(a,input("Enter password to decrypt:").encode())
    print(d)
    

