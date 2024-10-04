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
        # op=os.popen("light -A 10").read()
        # print(op)
    def decrease_bringtness(self):
        os.system("light -U 10")
    def wifi_on(self):
        os.system("nmcli radio wifi on")
        os.system('notify-send "Wifi on"')
    def wifi_off(self):
        os.system("nmcli radio wifi off")
        os.system('notify-send "Wifi off"')
    def show_wifi_list(self):
        os.system("nmcli device wifi list")
        # add function to show wifi list here  # TODO: implement this function
    def increase_volume(self):
        os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%")
        op=os.popen("pamixer --get-volume").read()
        os.system(f"notify-send 'vloume level is {op}'")
    def decrease_volume(self):
        os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%")
        op=os.popen("pamixer --get-volume").read()
        os.system(f"notify-send 'vloume level is {op}'")
    def mute(self):
        os.system("pactl set-sink-mute @DEFAULT_SINK@ toggle")
        op=os.popen("pamixer --get-mute").read()
        if op.strip()=="true":
            os.system('notify-send "muted"')
        else:
            os.system('notify-send "unmuted"')
        # print(op,type(op))
    def caps_lock(self):
        os.system("xdotool key Caps_Lock")
        op=os.popen('''xset q | grep "Caps Lock" | awk '{print ($4 == "on" ? "true" : "false")}' ''').read()
        if op.strip() == "true":
            os.system('notify-send "Caps Lock is on"')
        else:
            os.system('notify-send "Caps Lock is off"')

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
        button9=Button(self.root,text="mirror")
        button9.grid(row=3,column=3)
        label3=Label(text="sound")
        label3.grid(row=4,column=0)
        button10=Button(self.root,text="volume +",command=self.increase_volume)  
        button10.grid(row=5,column=0)
        button11=Button(self.root,text="volume -",command=self.decrease_volume)
        button11.grid(row=5,column=1)
        button12=Button(self.root,text="mute/unmute",command=self.mute)

        button12.grid(row=5,column=2)
        
        label4=Label(text="keyboard")
        label4.grid(row=6,column=0)
        button13=Button(self.root,text="caps lock",command=self.caps_lock)
        button13.grid(row=7,column=0)
        button14=Button(self.root,text="num lock")
        button14.grid(row=7,column=1)
        button15=Button(self.root,text="scroll lock")
        button15.grid(row=7,column=2)

        


if __name__ == "__main__":
    support()