from tkinter import *
root=Tk()
one = Label(root, text="One" , fg="red", bg="yellow")       #fg is forGround Color, and  bg is backGround color
one.pack()

two = Label(root, text="Two" , fg="white", bg="black") 
two.pack(fill=X)

three = Label(root, text="Three" , fg="green", bg="red") 
three.pack(side=LEFT,fill=Y)

four = Label(root, text="Four" , fg="white", bg="black") 
four.pack()

root.mainloop()