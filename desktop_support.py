from tkinter import *
import os
from sys import argv


class support:
    
    def __init__(self):
        self.root=Tk()
        self.root.bind("<Escape>",self.close_app)  # close app when escape button is clicked
        #root definition
        self.root_define()
        
        # call all the functions 
        self.add_button()

        # run root
        self.run_root()

    def root_define(self):
        self.hight=self.root.winfo_screenheight()
        self.width=self.root.winfo_screenwidth()
        self.root.title("system support")
        # print(self.hight,self.width)
        self.root.geometry(f"{self.width//2}x{self.hight//2}+{self.width//4}+{self.hight//4}")
    
    def increase_brightness(self):
        os.system("light -A 10")
    def decrease_bringtness(self):
        os.system("light -U 10")
    def wifi_on(self):
        os.system("nmcli radio wifi on")
        os.system('notify-send "Wifi on"')
    def wifi_off(self):
        os.system("nmcli radio wifi off")
        os.system('notify-send "Wifi off"')
    def show_wifi_list():
        pass
    def run_root(self):
        self.root.mainloop()


    def close_app(self,event):
        self.root.destroy()
    def add_button(self):
        label1=Label(text="controller")
        label1.grid(row=0,column=0)
        button1=Button(self.root,text="brightness +",command=self.increase_brightness)
        button1.grid(column=0,row=1)
        button2=Button(self.root,text="brightness -",command=self.decrease_bringtness)
        button2.grid(row=1,column=1)
        button3=Button(self.root,text="wifi on",command=self.wifi_on)
        button3.grid(row=1,column=2)
        button4=Button(self.root,text="wifi off",command=self.wifi_off)
        button4.grid(row=1,column=3)
        button5=Button(self.root,text="wifi list",command=self.show_wifi_list)
        button5.grid(row=1,column=4)
        label2=Label(text="display")
        label2.grid(row=2,column=0)
        button6=Button(self.root,text="laptop",)
        button6.grid(row=3,column=0)
        button7=Button(self.root,text="hdmi")
        button7.grid(row=3,column=1)
        button8=Button(self.root,text="both")
        button8.grid(row=3,column=2)
        


if __name__ == "__main__":
    support()