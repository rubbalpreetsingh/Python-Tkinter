#draw rectangle and line
from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
can= Canvas(root,width=200,height=200,bg="red")
can.pack()
line=can.create_line(0,0,200,100 )
line2=can.create_line(200,100,0,200,fill="white")

root.mainloop()