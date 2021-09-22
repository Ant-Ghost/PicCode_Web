from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

'''
This program is only used to create Initilization vector

'''



key = b'mysecretpassword' # 16 byte password

cipher = AES.new(key, AES.MODE_CBC)

plaintext=b'this is my super secret message '

ciphertext=cipher.encrypt((pad(plaintext,AES.block_size)))


with open("steg/VI_file",'wb') as c_file:
    c_file.write(cipher.IV)
