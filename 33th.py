# LableFrame 
from tkinter import *
root=Tk()
frame=LabelFrame(root,text="Input",padx=20,pady=40)
entry=Entry(frame)
entry.pack()
frame.pack()
root.geometry("400x400+120+120")
root.mainloop()