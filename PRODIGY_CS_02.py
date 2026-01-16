from tkinter import *
from tkinter import filedialog
gui=Tk()
gui.geometry("300x300")
gui.title("My first GUI")

def encryptor():
    filed=filedialog.askopenfile(mode='r',title='Select a file ',filetypes=[('','*png')])
    if filed is not None:
        file_pth=filed.name
        key=box1.get(1.0,END)
        print(f"you selected this {file_pth} with key: {key}")
        
        faa=open(file_pth,mode='rb')
        img_data=faa.read()
        faa.close()
        
        img_data=bytearray(img_data)

        for index,values in enumerate(img_data):
            img_data[index]=values^int(key)
        faah=open(file_pth,mode='wb')
        faah.write(img_data)
        faah.close()
    else:
        print("please select a Supported file type")


b1=Button(gui,text='Encrypt',command=encryptor)
b1.place(x=110,y=160)

box1=Text(gui,height=1,width=20)
box1.place(x=73,y=40)
gui.mainloop()