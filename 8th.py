# Working with classes
from tkinter import *
root=Tk()
 
class myButton:
    def __init__(self,master):
        self.printButton = Button(master, text="Print", command=self.printMsg)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(master,text="Quit", command=master.quit)
        self.quitButton.pack(side=LEFT)

    def printMsg(self):
        print("Hello")




b=myButton(root)
root.mainloop()