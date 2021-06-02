from tkinter import *
root=Tk()
root.geometry("300x300+250+250")
frame=Frame(root,width=300,height=300)
label=Label(frame,text="Hello",fg="red" ,bg="black")
label.pack()
frame.pack(side=BOTTOM)

root.mainloop()