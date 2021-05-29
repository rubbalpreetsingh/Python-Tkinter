#Binding function to Buttons



#from tkinter import *
#root =Tk()
#def callMe():
#    print("Button is Clicked")
#button=Button(root,text="Click Me", command=callMe)
#button.pack()
#root.mainloop()




from tkinter import *
root=Tk()
def callMe(event):
    print("Call Me")

button=Button(root,text="ClickMe")
button.bind("<Button-1>",callMe)
button.pack()
root.mainloop()
