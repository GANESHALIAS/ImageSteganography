import Imagesteganoraphy as ist
import Caesarcipher as c
import tkinter as tk






def en(imagep,ms,targp):
    emsg = c.encrypt((ms))
    e=ist.ImageSteg.encrypt_text_in_image(imagep,emsg,targp)

def de(imagep,targp):
    d=ist.ImageSteg.decrypt_text_in_image(imagep,targp)
    dmsg = c.decrypt(d)







