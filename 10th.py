# MessageBox
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400+120+120")
def callMe():
    #messagebox.showinfo("Success", "Installation complete")
    #messagebox.showwarning("Warning", "Do you want to exit")
    messagebox.showerror("Message","Not installed")

b=Button(root,text="Message", command=callMe)
b.pack()

root.mainloop()