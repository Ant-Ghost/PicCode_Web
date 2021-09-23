from PIL import Image
import os, sys
from .crypt import Crypting
import string
import base64


class Decode_Image:

    

    
    def __init__(self):
        self.decode_text=''
        self.error_decode=[0,'']



    def decideAndShow(self,bytes_decode):

        b64chars=string.ascii_lowercase+string.ascii_uppercase+string.digits+"+/=#"


        if len(bytes_decode)==8*4:
            four_char=''
            four_char_decode=[bytes_decode[i:i+8] for i in range(0, len(bytes_decode), 8)]
            for i in four_char_decode:
                four_char+=chr(int(i,2))
                if not ('#' in four_char):
                    self.error_decode[0]=-1
                    self.error_decode[1]="Image has no hidden text"
                    return True
                    
        text_decode=[bytes_decode[i:i+8] for i in range(0, len(bytes_decode), 8)]
        
        text = ''
        for i in text_decode:
            ch=chr(int(i,2))
            if not (ch in b64chars):
                self.error_decode[0]=-1
                self.error_decode[1]="Image has no hidden text"
                return True
            text+=ch
            if len(text) > 4:
                if text[-4:]=='####':
                    self.decode_text=text[4:-4]
                    return True

        return False


    def decode(self,im):
        try:
            pixels_list=list(im.getdata())
            index=0
            bytes_decode=''
            while True:
                pixel_tuple= pixels_list[index]
                # if type(pixel_tuple)!=tuple:
                #     pixel_tuple=tuple([pixel_tuple])
                index+=1
                        
                for i in range(0,len(pixel_tuple)):
                    bytes_decode+= str(pixel_tuple[i]&1)
                    if len(bytes_decode)>=8*4 and len(bytes_decode)%8==0 and self.decideAndShow(bytes_decode):
                        return
        except TypeError as e:
            print(e)
            self.error_decode[0]=-1
            self.error_decode[1]="IMAGE is corrupted. Try giving images with rgb format"
            return
            
            
    def stegano_decode(self,im_path,password):
        
        im = Image.open(im_path)
        self.decode(im)
        if self.error_decode[0]==0:
            password=password.encode();
            ciphertext=base64.b64decode(self.decode_text.encode())
            print("ciphertext: ",ciphertext)
            c_obj=Crypting()
            e,plaintext=c_obj.decrypting(ciphertext,password)
            print("plaintext: ",plaintext)
            print("error: ",e)
            if e==0:
                self.decode_text=plaintext
            else:
                self.error_decode[0]=-1
                self.error_decode[1]=plaintext
                print("error codes ", self.error_decode)
        im = im.close()


