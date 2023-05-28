#Write a Python GUI program to add a button in your application using tkinter module

from tkinter import *
win = Tk()
win.geometry('400x200')
def changetext():
a.config(text="HELLO WORLD")
a = Label(win, text="") 
but = Button(win, text="CLICK ME", command=changetext,pady=10,width=30,bg='#4caf50')
but.pack()
a.pack()
win.mainloop()
