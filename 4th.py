#GridLayout
from tkinter import *
root=Tk()
name=Label(root,text="Name")
password=Label(root,text="Password")
enteryOne=Entry(root)
enteryTwo=Entry(root)
name.grid(row=0,column=0,sticky=E)   # sticky is used to stick(Align) any think at edges ...u can use E for east, S for south
enteryOne.grid(row=0,column=1)
password.grid(row=1,column=0,sticky=E)  
enteryTwo.grid(row=1,column=1)



c=Checkbutton(root,text="Keep me LogIn")
c.grid(columnspan=2)
root.mainloop()