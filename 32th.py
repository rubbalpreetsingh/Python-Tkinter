#spinBox
from tkinter import *
root=Tk()
spin1=Spinbox(root,from_=1, to=5)
spin1.pack()
def enterCount():
    a=spin1.get()
    print(a)
button=Button(root,text="Click",command=enterCount)
button.pack()
root.geometry("400x400+120+120")
root.mainloop()