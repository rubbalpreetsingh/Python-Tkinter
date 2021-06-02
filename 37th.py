#Shortcut keys

from tkinter import *
from tkinter import messagebox
root=Tk()


def callMe(event=""):                  #every time when you bind function ----> you need to use ---> event
    messagebox.showinfo("Triying", "This is somthing important ")

button=Button(root,text="CallMe",command=callMe)
button.pack()
root.bind("<Control-c>",callMe)
root.geometry("400x400+120+120")
root.mainloop()