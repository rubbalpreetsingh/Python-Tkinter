# MessageBox- Ask Question
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400+120+120")

def clickFun():
    a=messagebox.askquestion("exit","Do you want to exit")      #Two option face --> yes or No --> yes value is yes and No value is NO
    if a=="yes":
        root.quit()


    


b=Button(root, text="Click", command=clickFun)
b.pack()


root.mainloop()