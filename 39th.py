from tkinter import *
root=Tk()
root.title("Calculator")

def enterNo(x):
    
    if entry.get()=="0":
        if x==".":
            entry.insert(1,".")
        else:
            entry.delete(0,END)
            entry.insert(0,str(x))
    else:
        length=len(entry.get())
        entry.insert(length,str(x))


#EntyBox---
entry=Entry(font="vardana 14 bold",width=28,bd=6,justify=RIGHT)
entry.insert(0,"0")
btnNo=[]
for i in range(10):
    btnNo.append(Button(width=4,text=str(i),bd=6,command=lambda x=i: enterNo(x)))

btnText=1
for i in range(0,3):
    for j in range(0,3):
        btnNo[btnText].place(x=30+j*90,y=70+i*70)
        btnText+=1
entry.place(x=30, y=10)


# Operators Buttons

def enterOperator(x):
    if entry.get() !="0":
        length=len(entry.get())
        allText=entry.get()
        lastChar=allText[-1:]
        if lastChar in ["+","-","/"] or allText=="**":
            pass
        else:
            entry.insert(length,btnOpr[x]["text"])


btnOpr=[]
for i in range(4):
    btnOpr.append(Button(width=4,font="time 14 bold",bd=4,command=lambda x=i: enterOperator(x)))
btnOpr[0]["text"]="+"
btnOpr[1]["text"]="-"
btnOpr[2]["text"]="*"
btnOpr[3]["text"]="/"

for i in range(4):
    btnOpr[i].place(x=290, y=70+i*70)



#btn zero

btn_zero=Button(width=30,text="0",bd=5,command=lambda x=0: enterNo(x))
btn_zero.place(x=30,y=280)



#btn clear


def clearFun():
    entry.delete(0,END)
    entry.insert(0,"0")

btn_clear=Button(width=4,text="C",font="times 15 bold", bd=5,command=clearFun)
btn_clear.place(x=25,y=340)



# . button
btn_dot=Button(width=4,text=".",font="times 15 bold", bd=5,command=lambda x=".": enterNo(x))
btn_dot.place(x=110,y=340)


# = button

result=0
history=[]
def funEqual():
    content=entry.get()
    result=eval(content)
    print(result)
    entry.delete(0,END)
    entry.insert(0,result)
    history.append(content)
    history.reverse()
    status.configure(text="History: "+" | " .join(history[0:4]),font="verdana 10 bold")


btn_equal=Button(width=4,text="=",font="times 15 bold", bd=5,command=funEqual)
btn_equal.place(x=200,y=340)



# delete button
def funDel():
    lengeth=len(entry.get())
    entry.delete(lengeth-1)
    if lengeth==1:
        entry.insert(0,"0")

btn_del=Button(width=4,text="del",font="times 15 bold", bd=5,command=funDel)
btn_del.place(x=290,y=340)



#HISTORY

status=Label(root,text="History",relief=SUNKEN,height=3,anchor=W,font="verdana 11 bold")
status.pack(side=BOTTOM,fill=X)


root.geometry("380x550+120+120")
root.resizable(FALSE,FALSE)  #means , now u can not resize the window x-axis or y-axis
root.mainloop()