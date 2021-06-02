from tkinter import *

from tkinter import filedialog

class textEditor:
    currentOpenFile="noFile"
    def openFile(self):
        openReturn=filedialog.askopenfile(initialdir="c:",title="Select File to open", filetypes=(("text files","*.txt"),("all files","*.*")))
        if(openReturn!=None):
            self.textArea.delete(1.0,END)  #1.0 means first line first char
            for line in openReturn:
                self.textArea.insert(END,line)
            self.currentOpenFile=openReturn.name    #the name of opened file is going to currentOpenFile var
            openReturn.close()

    def saveFile(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        text2save=self.textArea.get(1.0,END)
        self.currentOpenFile=f.name
        f.write(text2save)
        f.close()

    def save(self):
        if self.currentOpenFile=="noFile":
            self.saveFile()
        else:
            f=open(self.currentOpenFile,"w+")
            f.write(self.textArea.get(1.0,END))
            f.close()

    def newFile(self):
        self.textArea.delete(1.0,END)
        self.currentOpenFile="noFile"


    def copyText(self):
        self.textArea.clipboard_clear()
        self.textArea.clipboard_append(self.textArea.selection_get())


    def cutText(self):
        self.copyText()
        self.textArea.delete("sel.first","sel.last")    #that is our selected text first index to last index

    def pasteText(self):
        self.textArea.insert(INSERT,self.textArea.clipboard_get())



    def __init__(self,master):
        self.master=master
        master.title("Text Editor")
        self.textArea= Text(self.master,undo=True)
        self.textArea.pack(fill=BOTH,expand=1)
        self.mainMenu=Menu()
        self.master.config(menu=self.mainMenu)

        #Creating FileMenu
        self.fileMenu=Menu(self.mainMenu,tearoff=FALSE)
        self.mainMenu.add_cascade(label="File",menu=self.fileMenu)

        self.fileMenu.add_cascade(label="New",command=self.newFile)
        self.fileMenu.add_command(label="Open",command=self.openFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_cascade(label="Save",command=self.save)
        self.fileMenu.add_cascade(label="Save As",command=self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_cascade(label="Exit",command=master.quit)
        

        #Creating EditMenu
        self.editMenu=Menu(self.mainMenu,tearoff=FALSE)
        self.mainMenu.add_cascade(label="Edit",menu=self.editMenu)
        self.editMenu.add_cascade(label="Undo",command=self.textArea.edit_undo)
        self.editMenu.add_cascade(label="Redu",command=self.textArea.edit_redo)
        self.editMenu.add_separator()
        self.editMenu.add_cascade(label="Copy",command=self.copyText)
        self.editMenu.add_cascade(label="Cut",command=self.cutText)
        self.editMenu.add_cascade(label="Paste",command=self.pasteText)


root=Tk()
te=textEditor(root)

root.mainloop()