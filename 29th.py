#Input through popup window

from tkinter import *
from tkinter import simpledialog
root=Tk()
def popUP():
    z=simpledialog.askstring("Input String","Please Enter Yout Name")   #You can also take-----> askInt , askfloat
    print(z)
button=Button(root,text="PopUp",command=popUP)
button.pack()
root.geometry("400x400+120+120")
root.mainloop()