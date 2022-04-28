#Fourth project
'''Exe Clock'''
from tkinter import *
from tkinter.ttk import *

from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#Design

root = Tk()
root.title("Clock by ExE")


label = Label(root, font=("ds-digital" , 80), background = "black" , foreground = "cyan") 
label.pack(anchor='center')

time()

mainloop()


