
#Write a Python GUI program to create a Checkbutton widget using tkinter module.

from tkinter import *
win=Tk()
win.geometry('400x300')
v1=IntVar()
v2=IntVar()
def show():
 if v1==1 and v2==0:
 a1.config(text="so you love c++")
 elif v1==0 and v2==1:
 a1.config(text="so you love python")
 else:
 a1.config(text="so you love c++ and python")
a1 = Label(win, text="") 
c1=Checkbutton(win,text="c++",variable=v1,onvalue=1, offvalue=0,height=3)
c2=Checkbutton(win,text="PYTHON",variable=v2,onvalue=1, offvalue=0,height=3)
but1 = Button(win, text="Submit", command=show,pady=10,width=30,bg='#4caf50')
c1.pack()
c2.pack()
but1.pack()
a1.pack()
win.mainloop()
