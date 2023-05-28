
#Write a Python GUI program to create a Listbox bar widgets using tkinter module.

from tkinter import *
parent =Tk()
parent.geometry("400x300")
label1 =Label(parent,text = "A list of tkinter function")
listbox =Listbox(parent)
listbox.insert(1,"BUTTON")
listbox.insert(2, "LABEL1")
listbox.insert(3, "DESTROY")
listbox.insert(4, "PACK")
label1.pack()
listbox.pack()
parent.mainloop() 

