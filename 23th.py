#Listbox
#ByDefault width=20 ... means it can take 20char 
#Bydefault height=10 ...means 10 items 
from tkinter import *
root=Tk()
root.geometry("400x400+120+120")
l=Listbox(root,height="20",width="40",selectmode=EXTENDED)     #default mode=BROWSE     1=SINGLE    2=MULTIPLE   3=EXTENDED
l.insert(1,"C")
l.insert(2,"C++")
l.insert(3,"Java")
l.insert(4,"Python")
l.insert(5,"Dart")
l.insert(6,"SQL")
l.insert(7,"HTML")
l.insert(8,"CSS")
l.insert(9,"JavaScript")
l.insert(10,"Flutter")
l.insert(11,"TKinter")
l.insert(12,"ppp")
l.pack()
def PrintMe():
    clickedItems=l.curselection()
    #print(clickedItems)
    for i in clickedItems:
        print(l.get(i))
button=Button(root,text="Enter" , command=PrintMe)
button.pack()
def delete_me():
    clickedItems=l.curselection()
    for i in clickedItems:
        print(l.delete(i))

button_del=Button(root,text="Delete",command=delete_me)
button_del.pack()
root.mainloop()