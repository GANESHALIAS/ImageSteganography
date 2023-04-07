from ImageSteg import ImageSteg
import Caesarcipher as c
from tkinter import *
from tkinter import messagebox

img=ImageSteg()
def action():
    x = option.get()
    if x == 1:
        imagepx = imageptxt.get()
        messagex= messagetxt.get()
        targetx = targettxt.get()

        image = str(imagepx)
        message = str(messagex)
        target = str(targetx)

        emsg=c.encrypt(message)
        e=img.encrypt_text_in_image(image,emsg,target)

        messagebox.showinfo('Enrypted')

    if x == 2:
        imageppx = imagepptxt.get()
        imagepp = str(imageppx)

        d=img.decrypt_text_in_image(imagepp)
        dmsg=c.decrypt(d)
        messagebox.showinfo('Decrypted message = ',dmsg)

def encr():
    decrypt_frame.grid_forget()
    encrypt_frame.grid(row=1, column=0)

def decr():
    encrypt_frame.grid_forget()
    decrypt_frame.grid(row=1, column=0)

window = Tk()

window.title("Image Stagenography")
window.geometry('450x300')

option = IntVar()

Radiobutton(window, text="Encrypt", variable=option, value=1, command=encr).grid(column=0, row=0)
Radiobutton(window, text="Decrypt", variable=option, value=2, command=decr).grid(column=1, row=0)

encrypt_frame = Frame(window)
decrypt_frame = Frame(window)

imagelbl = Label(encrypt_frame, text="Enter the image path: ", padx=5, pady=5)
messagelbl = Label(encrypt_frame, text="Enter the message: ", padx=5, pady=5)
targetlbl = Label(encrypt_frame, text="Enter the target path: ", padx=5, pady=5)

imagepplbl = Label(decrypt_frame, text ="Enter the image path: ", padx=5, pady=5)

imageptxt = Entry(encrypt_frame, width=10)
messagetxt = Entry(encrypt_frame, width=10)
targettxt = Entry(encrypt_frame, width=10)

imagepptxt = Entry(decrypt_frame, width=10)

actbtn = Button(window, text="Action", command=action, padx=5, pady=5)
quitbtn = Button(window, text="Quit", command=window.destroy)


imagelbl.grid(column=0, row=0)
messagelbl.grid(column=0, row=1)
targetlbl.grid(column=0, row=2)
imagepplbl.grid(column=0, row=0)
imageptxt.grid(column=1, row=0)
messagetxt.grid(column=1, row=1)
targettxt.grid(column=1, row=2)
imagepptxt.grid(column=1, row=0)

actbtn.grid(column=1, row=1)
quitbtn.grid(column=1, row=2)

window.mainloop()
