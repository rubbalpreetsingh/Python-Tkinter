#ComboBox

from tkinter import *
from tkinter.ttk import *   
root=Tk()
root.geometry("400x400+120+120")
#v=["C","C++","Java"]
v=list(range(1,31))    #for days
c=Combobox(root,value=v,height=20,width=15)
c.set("Select")
c.pack()
def printFun():
    v=c.get()
    print(v)
button=Button(root,text="Enter",command=printFun)
button.pack()
root.mainloop()