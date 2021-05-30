#messagebox ask question Part-2
from tkinter import *
from tkinter import messagebox
def butFun():
    a=messagebox.askyesnocancel("Exit", "Do you want to exit")  # face 3 options --> yes, No , Cancel--> yes value is True, No value is False, cancel value is None
    if a=="True":
        root.quit()
    #messagebox.askretrycancel()

root=Tk()
root.geometry("400x400+120+120")
button=Button(root,text="Click", command=butFun)
button.pack()

root.mainloop()
