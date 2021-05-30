#to draw an arc on Canvas
from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
can=Canvas(width=400,height=400,bg="red")
can.pack()

can.create_arc(100,100,200,200,extent=120)

root.mainloop()