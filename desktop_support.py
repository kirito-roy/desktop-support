from tkinter import *
import os
from functools import partial
from sys import argv
from style1 import Sbutton

class support:
    
    def __init__(self):
        self.root = Tk()
        self.root.bind("<Escape>", self.close_app)  # Close app when escape button is clicked
        
        # Root definition
        self.root_define()
        self.add_frame()
        
        # Call all the functions 
        self.add_button()

        # Run root
        self.run_root()

    def root_define(self):
        self.height = self.root.winfo_screenheight()
        self.width = self.root.winfo_screenwidth()
        self.root.title("System Support")
        self.root.geometry(f"{self.width//2}x{self.height//2}+{self.width//4}+{self.height//4}")
        
        self.sb = Scrollbar(self.root)  
        self.sb.pack(side=RIGHT, fill=Y)

    def add_frame(self):
        # Create a canvas to hold a frame
        self.canvas = Canvas(self.root, yscrollcommand=self.sb.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a frame inside the canvas
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # Configure the scrollbar
        self.sb.config(command=self.canvas.yview)

        # Update the scroll region when widgets are added
        self.frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        # Update scroll region to encompass the entire frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
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
        wifi_list = os.popen("nmcli -t -f SSID device wifi list").read()
        self.wifi_list.config(text=wifi_list)
        self.button5.config(text="hide list",command=self.hide_wifi_list)
        # print(list.read())
        # add function to show wifi list here  # TODO: implement this function
    def hide_wifi_list(self):
        self.wifi_list.config(text="")
        self.button5.config(text="wifi list" , command=self.show_wifi_list)
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
    def num_lock(self):
        os.system("xdotool key Num_Lock")
        op=os.popen('''xset q | grep "Num Lock" | awk '{print ($4 == "on" ? "true" : "false")}' ''').read()
        if op.strip() == "true":
            os.system('notify-send "Num Lock is on"')
        else:
            os.system('notify-send "Num Lock is off"')
    def scroll_lock(self):
        os.system("xdotool key Scroll_Lock")
        op=os.popen('''xset q | grep "Scroll Lock" | awk '{print ($4 == "on" ? "true" : "false")}' ''').read()
        if op.strip() == "true":
            os.system('notify-send "Scroll Lock is on"')
        else:
            os.system('notify-send "Scroll Lock is off"')

    def show_vpn_list(self):
        self.vpn_list.grid(row=11,column=0, columnspan=5, sticky='W')
        # Execute the command and get the VPN list
        vpn_list = os.popen("nmcli -t -f NAME,TYPE connection show | grep vpn | cut -d: -f1").read()
        vpn_list = vpn_list.strip().split('\n')

        # Print the list (for debugging purposes)
        print(vpn_list)

        # Loop through each VPN and create a button
        for vpn_name in vpn_list:
            b = Sbutton(self.vpn_list, text=vpn_name)
            
            # Use partial to pass the correct vpn_name to the command
            b.config(command=partial(self.select_vpn, vpn_name=vpn_name))
            b.pack()

        # Optional: Update the button to hide the list (if needed)
        self.button16.config(text="hide list", command=self.hide_vpn_list)
    def hide_vpn_list(self):
        self.button16.config(text="wifi list" , command=self.show_vpn_list)
        self.vpn_list.grid_forget()

    selected_vpn=list()
    def select_vpn(self, vpn_name):
        print(vpn_name)
        self.selected_vpn.append(vpn_name)
    def connect_vpn(self):
        if self.selected_vpn!="":
            os.system(f"nmcli con up {self.selected_vpn[len(self.selected_vpn)-1]}")
            os.system('notify-send "VPN connected"')
        else:
            os.system('notify-send "Please select a VPN"')
    def disconnect_vpn(self):
        os.system(f"nmcli con down {self.selected_vpn.pop()} ")
        os.system('notify-send "VPN disconnected"')
    def run_root(self):
        self.root.mainloop()


    def close_app(self,event):
        self.root.destroy()
    def add_button(self):
        label1=Label(self.frame,text="controller")
        label1.grid(row=0,column=0)
        button1=Sbutton(self.frame,text="brightness +",command=self.increase_brightness)
        button1.grid(column=0,row=1)
        button2=Sbutton(self.frame,text="brightness -",command=self.decrease_bringtness)
        button2.grid(row=1,column=1)
        button3=Sbutton(self.frame,text="wifi on",command=self.wifi_on)
        button3.grid(row=1,column=2)
        button4=Sbutton(self.frame,text="wifi off",command=self.wifi_off)
        button4.grid(row=1,column=3)
        self.button5=Sbutton(self.frame,text="wifi list",command=self.show_wifi_list)
        self.button5.grid(row=1,column=4)
        self.wifi_list=Label(self.frame)
        self.wifi_list.grid(row=2,column=0, columnspan=5, sticky='W')
        label2=Label(self.frame,text="display")
        label2.grid(row=3,column=0)
        button6=Sbutton(self.frame,text="laptop",)
        button6.grid(row=4,column=0)
        button7=Sbutton(self.frame,text="hdmi")
        button7.grid(row=4,column=1)
        button8=Sbutton(self.frame,text="both")
        button8.grid(row=4,column=2)
        button9=Sbutton(self.frame,text="mirror")
        button9.grid(row=4,column=3)
        label3=Label(self.frame,text="sound")
        label3.grid(row=5,column=0)
        button10=Sbutton(self.frame,text="volume +",command=self.increase_volume)  
        button10.grid(row=6,column=0)
        button11=Sbutton(self.frame,text="volume -",command=self.decrease_volume)
        button11.grid(row=6,column=1)
        button12=Sbutton(self.frame,text="mute/unmute",command=self.mute)
        button12.grid(row=6,column=2)
    
        label4=Label(self.frame,text="keyboard")
        label4.grid(row=7,column=0)
        button13=Sbutton(self.frame,text="caps lock",command=self.caps_lock)
        button13.grid(row=8,column=0)
        button14=Sbutton(self.frame,text="num lock",command=self.num_lock)
        button14.grid(row=8,column=1)
        button15=Sbutton(self.frame,text="scroll lock",command=self.scroll_lock)
        button15.grid(row=8,column=2)
        label5=Label(self.frame,text="VPN")
        label5.grid(row=9,column=0)
        self.button16=Sbutton(self.frame,text="VPN list",command=self.show_vpn_list)
        self.button16.grid(row=10,column=0)
        button17=Sbutton(self.frame,text="connect VPN",command=self.connect_vpn)
        button17.grid(row=10,column=1)
        button18=Sbutton(self.frame,text="disconnect VPN",command=self.disconnect_vpn)
        button18.grid(row=10,column=2)
        self.vpn_list=Frame(self.frame,)
        label6=Label(self.frame,text="power")
        label6.grid(row=12,column=0)
        button19=Sbutton(self.frame,text="lock screen")
        button19.grid(row=13,column=0)
        button20=Sbutton(self.frame,text="logout")
        button20.grid(row=13,column=1)
        button21=Sbutton(self.frame,text="shutdown")
        button21.grid(row=13,column=2)
        button22=Sbutton(self.frame,text="restart")
        button22.grid(row=13,column=3)

        


if __name__ == "__main__":
    support()
