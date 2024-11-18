from tkinter import *
import pyjokes
from tkinter import ttk, messagebox
import tkinter as tk

root = Tk()


root.configure(bg="#e4d8f2")
root.title("Do you want to hear a joke?")
root.geometry("600x450")


label=Label(root, text="TIME TO LAUGH" ,font=("chiller", 33, "bold"),bg="#e4d8f2")
label.place(relx=0.5, rely=0.1, anchor= CENTER)

label2=Label(root, text="PICK YOUR JOKES!",font=("chiller", 23, "bold"),bg="#e4d8f2")
label2.place(relx=0.5, rely=0.25, anchor= CENTER)


category_var=StringVar()
combo = ttk.Combobox(root, textvariable=category_var, state="readonly", font=("chiller",11))
combo['values']=['Programming','Chuck','Random']
combo.place(relx=0.5, rely=0.35, anchor= CENTER)

def getjoke():
    category=category_var.get()
    joke=""
    if category == "Programming":
        joke=pyjokes.get_joke(category="neutral")
        
    elif category == "Chuck":
        joke=pyjokes.get_joke(category="chuck")
        
        
    else  : 
        joke=pyjokes.get_joke()
        
    labelj['text']=joke  
        
        
     
BTNJOKEEE=Button(root,text="PRESS HERE FOR A JOKE", bg="#ffbabe", command=getjoke)
BTNJOKEEE.place(relx=0.5, rely=0.45, anchor= CENTER)

labelj=Label(root,font=("chiller", 19, "bold"),bg="#e4d8f2", wraplength=500)
labelj.place(relx=0.5, rely=0.55, anchor= CENTER)

def hep():
    messagebox.showinfo("Help", "Select a category from the dropdown, then hit the button!")

BTNHELPPP=Button(root,text="Help",font=("chiller"),bg="#ffbabe", command=hep)
BTNHELPPP.place(relx=0.5, rely=0.75, anchor= CENTER)










root.mainloop()