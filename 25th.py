#Font   NOt Working 

from tkinter import *
from tkinter.font import Font
root=Tk()
root.geometry("400x400+120+120")
my_ont=Font(size=56,fg="red")
label=Label(root,text="Crazy Mind", font="25").pack()
root.mainloop()
