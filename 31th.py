# Work with the multiple windows 
from tkinter import *
def goFun():
    go=Toplevel()
    go.title("This is new window")
    go.geometry("400x400+120+120")
    def exitGO():
        go.destroy()      #to close the window --use---> destroy()
    button1=Button(go,text="Exit",command=exitGO)
    button1.pack()
root=Tk()
root.geometry("400x400+120+120")
button=Button(root,text="Go",command=goFun)
button.pack()
root.mainloop()