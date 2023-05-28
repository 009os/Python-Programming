

#Write a Python GUI program to create a calculator (have button for Addition and subtraction) using 
#tkinter module.

from tkinter import *
frame = Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
def sub():
 a=int(input1.get('1.0'))
 b=int(input2.get('1.0')) 
 lbl.config(text=a-b)
def add():
 a=int(input1.get('1.0'))
 b=int(input2.get('1.0'))
 
 lbl.config(text=a+b)
input1 = Text(frame,height = 1,width = 20)
input2 = Text(frame,height = 1,width = 20)
sub = Button(frame,text = "SUBTRACT",command = sub,height=1,width=20,bg='#4caf50')
add = Button(frame,text = "ADITION",command = add,height=1,width=20,bg='#4caf50')
lbl = Label(frame, text = "")
lb2 = Label(frame, text = "NUM1")
lb3 = Label(frame, text = "NUM2")
lb2.pack()
input1.pack()
lb3.pack()
input2.pack()
sub.pack()
add.pack()
lbl.pack()
frame.mainloop()

