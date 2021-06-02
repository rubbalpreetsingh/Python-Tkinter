#FileDialog box   -to save file
from tkinter import *
from tkinter import filedialog
root=Tk()
def saveFile():
    r=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if r is None:
        return 
    r.write("Hello")
    r.close()
button=Button(root,text="Save File",command=saveFile) 
button.pack()
root.geometry("400x400+120+120")
root.mainloop()