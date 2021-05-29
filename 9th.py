from tkinter import *
root=Tk()
root.geometry("300x300+120+120")
mainMenu=Menu(root)
root.config(menu=mainMenu)


def newProject():
    print("New Project")
def moreMenuPrint():
    print("New More")

#File Menu
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project", command=newProject)
fileMenu.add_command(label="Old Project", command=newProject)
fileMenu.add_separator()
fileMenu.add_command(label="Open", command=newProject)
fileMenu.add_command(label="Exit", command=newProject)

moreMenu=Menu(fileMenu)
fileMenu.add_cascade(label="More",menu=moreMenu)
moreMenu.add_command(label="Saved File", command=moreMenuPrint)
moreMenu.add_command(label="Deleted File", command=moreMenuPrint)



#Edit Menu
editMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)

root.mainloop()