from PIL import Image
import os, sys
from .crypt import Crypting
import base64


class Encode_Image:


    error_encode=[0,'']

    def __init__(self):
        pass



    def msg_to_bytes(self,msg):

        if type(msg)==str:
            return ''.join([format(ord(i),"08b") for i in msg])

        if type(msg)==tuple:
            return [format(i,'08b') for i in msg]
        
        if type(msg)==int:
            return format(msg,'08b')




    def encode(self,im, msg):
        try:
            pixels=im.load()
            pixels_list=list(im.getdata())
            index_p=0
            index_msg=0

            bytes_msg=self.msg_to_bytes(msg)
            

            for i in range(im.size[0]):
                for j in range(im.size[1]):
                    if (index_msg==len(bytes_msg)):
                        return

                    
                    pixel_arr=self.msg_to_bytes(pixels_list[index_p])
                    index_p+=1
                    
                    
                    
                    for x in range(0,len(pixel_arr)):
                        
                        if index_msg<len(bytes_msg):
                            pixel_arr[x]=pixel_arr[x][:-1]+bytes_msg[index_msg]
                            index_msg+=1
                        pixel_arr[x]=int(pixel_arr[x],2)
                    pixels[j,i]=tuple(pixel_arr)
        except TypeError as e:
            print(e)
            self.error_encode[0]=-1
            self.error_encode[1]="IMAGE is corrupted. Try giving images with rgb format"
            return


    def stegano_encode(self, secret_message,password, im_path):
        
        
        c_obj=Crypting()


        secret_message=secret_message.encode()
        password=password.encode()

        secret_message=base64.b64encode(c_obj.encrypting(password,secret_message)).decode()
        secret_message="####"+secret_message+"####"
        print(secret_message)
        while True:
            print("Checking path....", end='')
            if os.path.exists(im_path):
                break
            else:
                self.error_encode[0]=-1;
                self.error_encode[1]="Server error"
                return
        
        #Opening Image
        im = Image.open(im_path)

        f= im.format
        if f=='JPEG':
            f = 'PNG'

        #if not (im.mode=='RGB' or im.mode=='RGBA'):
        #    print(bc.FAIL+"Only RGB or RGBA modes supported..... Exiting"+bc.ENDC)
        #    return

        fn, fext= os.path.splitext(im_path)
        
        #Comparing image size(pixels) and message length(characters) [no. of pixels >= no. of characters]
        print("Comparing Image size and Message Length...",end='')
        w, h= im.size
        size=w*h
        if size < len(secret_message):
            self.error_encode[0]=-1;
            self.error_encode[1]="Message too big to fit in Image"
            return
        
        self.encode(im, secret_message)
        
        new_save= fn+fext

        
        im.save(new_save,f)

        im.close()

        return


