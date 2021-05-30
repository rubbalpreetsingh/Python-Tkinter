#create Oval
from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
can = Canvas(height=400,width=400,bg="red")
can.pack()
can.create_rectangle(100,100,300,250,fill="yellow",outline="black")
can.create_oval(100,100,300,250)
root.mainloop()