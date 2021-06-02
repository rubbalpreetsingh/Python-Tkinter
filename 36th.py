#colorchosser -color Dialog

from tkinter import *
from tkinter import colorchooser
root=Tk()
def colorFun():
    c=colorchooser.askcolor(title="Select Color")
    root.configure(bg=c[1])
    print(c)
button=Button(root,text="Change Color",command=colorFun)
button.pack()
root.geometry("400x400+120+120")
root.mainloop()