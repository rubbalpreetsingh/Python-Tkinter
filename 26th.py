#Text Box Big
from tkinter import *
def enterFun():
    #result=text.get(1.0,END)
    result=text.selection_get()    # More methods 
    pos = text.search(result , 1.0,stopindex=END)    
    print(pos)
    print(result)

def clearFun():
    text.delete(1.0,END)
root=Tk()
text=Text(root,width=20,height=10,wrap=WORD,padx=10,pady=10, bd=4, selectbackground="red" )   #height= no. of lines to show ,,, width = no of char in row   #wrap=WORD is used for take the char ino new line, So that our word can-not cut             #padx is for padding from left-x                  #pady---> is for padding top-y       # bd of border width ----> By default bd=2                   #selectbackground --> is for select color 
text.insert(INSERT,"HELLO")
text.pack()                
button=Button(root,text="Enter", command=enterFun)       
button.pack()                     
button2=Button(root,text="Clear",command=clearFun)
button2.pack()
root.geometry("400x400+120+120")                       
root.mainloop()