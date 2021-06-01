# RadioButton

from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
def ckeckFun():
    if( i.get()==1):
        print("Male")
    else:
        print("Female")

i=IntVar()
r1=Radiobutton(root,text="Male",value=1,variable=i)
r2=Radiobutton(root,text="Female",value=2,variable=i)
r1.pack()
r2.pack()
button=Button(root,text="Click", command=ckeckFun)
button.pack()
root.mainloop()