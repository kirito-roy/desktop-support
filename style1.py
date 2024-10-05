from tkinter import *

def none():
    pass

def Sbutton(root,text,command=none):
    return Button(root,text=text,command=command,
                  background="#ff11ee",
                  foreground="#ffffff",
                  borderwidth="0",
                  relief="flat",
                  overrelief="groove",
                  cursor="hand2",
                  width="20",
                  height="2",
                  font=("impact", 11))