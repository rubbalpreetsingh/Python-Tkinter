#Part Two
# How to get the value of Entry   with the help of StringVar funtion
# You can also set the value in Entry with the help of set function

from tkinter import *
root=Tk()

def clickFun():
    s1=entry.get()
    print(s1)
root.geometry("400x400+120+120")
s=StringVar()
entry=Entry(root,textvariable=s)
entry.pack()
s.set("Welcome")
button=Button(root,text="Click",command=clickFun)
button.pack()
print(s)
root.mainloop()