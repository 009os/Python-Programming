
#Write a Python GUI program to create: a Loginform using tkinter module.

from tkinter import *
frame = Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
def printInput():
lbl.config(text = "YOU ARE LOGGED IN SUCCESSFULLY...")
input1 = Text(frame,height = 1,width = 20)
input2 = Text(frame,height = 1,width = 20)
show = Button(frame,text = "LOGIN",command = printInput,height=1,width=20,bg='#4caf50')
lbl = Label(frame, text = "")
lb2 = Label(frame, text = "Username")
lb3 = Label(frame, text = "Password")
lb2.pack()
input1.pack()
lb3.pack()
input2.pack()
show.pack()
lbl.pack()
frame.mainloop()

