# Geometry Managers-
#    in tkinter there are three types of Geometry Managers
#       1- pack()  2-grid()  3-place()

from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
label1=Label(root,text="Text1")
label2=Label(root,text="Text2")
label1.place(x=200,y=200)    #it takes the two argument that is ==> x and y
label2.place(x=200,y=220)
root.mainloop()