#ScrollBar 

from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
scrol=Scrollbar(frame)
scrol.pack(side=RIGHT,fill=Y)
listbox=Listbox(frame,yscrollcommand=scrol.set)
for i in range(1 , 100):
    listbox.insert(END,"List"+str(i))
listbox.pack(side=LEFT)
scrol.config(command=listbox.yview)
root.mainloop()