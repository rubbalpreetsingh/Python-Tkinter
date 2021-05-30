#Canvas-Image
from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
can=Canvas(height=400,width=400,bg="red")
can.pack()
photo=PhotoImage(file="D:\\HTML CSS\\Crazy Mind\\Images\\flutter.png")
can.create_image(0,0,image=photo, anchor=NW)  

root.mainloop()