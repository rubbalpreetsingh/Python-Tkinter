#Part one
# How to get the value of Entry   with the help of get funtion

from tkinter import *
def clickMe():
    z=entry.get()
    if z=="Hello":
        print("Done")
root=Tk()
root.geometry("400x400+120+120")
entry=Entry(root)
entry.pack()
button=Button(root,text="Go" , command=clickMe)
button.pack()
root.mainloop()