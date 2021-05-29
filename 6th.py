from tkinter import *
root=Tk()
def rightClick(event):
    print("Right Click")


def leftClick(event):
    print("Left Click")

def middelClick(event):
    print("Middel click")

frame=Frame(root,width=300,height=300)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>" ,middelClick)
frame.bind("<Button-3>" ,rightClick)
frame.pack()
root.mainloop()