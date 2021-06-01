#slider or scale
from tkinter import *
root=Tk()
s=Scale(root,from_ =0 , to= 100, orient=HORIZONTAL,width=8,sliderlength=10)  #by default it create vertical slider-----> to change into horizontal use->orient     #By default its length is 100  and width is 15           #sliderlength by default 30
s.set(50)
s.pack(fill=X)
a=s.get()
print(a)

root.geometry("400x400+120+120")
root.mainloop()