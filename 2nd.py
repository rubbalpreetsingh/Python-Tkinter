from tkinter import *
r=Tk()
frame=Frame(r)
button1=Button(frame,text="Click1")
button2=Button(frame,text="Click2")
button3=Button(frame,text="Click3")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
frame.pack()


bottomFrame=Frame(r)
button4=Button(bottomFrame,text="Bottom1")
button4.pack()
bottomFrame.pack(side=BOTTOM)
r.mainloop()