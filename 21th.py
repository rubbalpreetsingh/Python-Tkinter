# checkbutton

from tkinter import *
root=Tk()
def checkFun():
    print(i.get())
i=IntVar()
root.geometry("400x400+120+120")
c=Checkbutton(root,text="Item 1",variable=i)     # if checkbutton is checked then the value is 1 .. else 0
button=Button(root,text="Click",command=checkFun)
button.pack()
c.pack()

root.mainloop()