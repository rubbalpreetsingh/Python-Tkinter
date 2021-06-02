#FileDialog box   -to open file 
from tkinter import *
from tkinter import filedialog
def openFile():
    z=filedialog.askopenfile(initialdir="D:\\",title="Select File",filetypes=(("text files",".txt"),("all files","*.*")))
    for c in z:
        print(c)    #it prints the text inside that file
root=Tk()
button=Button(root,text="Open File", command=openFile)
button.pack()
root.geometry("400x400+120+120")
root.mainloop()