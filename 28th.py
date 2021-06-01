#Searching Software
from tkinter import *
import wikipedia

def getData():
    enteredValue=entry.get()
    text.delete(1.0,END)
    try:
        answerValue=wikipedia.summary(enteredValue)
        text.insert(INSERT,answerValue)
    except:
        text.insert(INSERT,"Check what you input or internet connection")

root=Tk()
topFrame=Frame(root)
entry=Entry(topFrame)
entry.pack()
button=Button(topFrame,text="Search",command=getData)
button.pack()
topFrame.pack(side=TOP)


bottomFrame=Frame(root)
scroll=Scrollbar(bottomFrame)
scroll.pack(side=RIGHT, fill=Y)
text=Text(bottomFrame,width=30,height=10, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=text.yview)
text.pack()




bottomFrame.pack(side=BOTTOM)
root.geometry("400x400+120+120")
root.mainloop()